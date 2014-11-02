from rest_framework import status

from users.models import User
from .base import RestClientTest


class CoreDataRestClientAccessTest(RestClientTest):

    def test_anyone_can_access_the_api(self):
        response = self.client.get(self.server_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anyone_can_access_all_users(self):
        response = self.client.get(self.server_url + '/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anyone_can_create_a_user_with_valid_information(self):
        signup_data = {'email': 'edith@e.org', 'password': 'ee', 'handle': 'edith', 'name': 'Evocative Edith'}
        response = self.client.post(self.server_url + '/users/', signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], signup_data['email'])
        self.assertEqual(response.data['handle'], signup_data['handle'])
        self.assertEqual(response.data['name'], signup_data['name'])

    def test_no_one_can_create_a_user_with_insufficient_information(self):
        signup_data_missing_name = {'email': 'edith@e.org', 'password': 'ee', 'handle': 'edith'}
        response = self.client.post(self.server_url + '/users/', signup_data_missing_name)
        self.assertEqual(User.objects.count(), 4)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'name': ['This field is required.']}
        self.assertEqual(response.data, data)

        signup_data_missing_password = {'email': 'edith@e.org', 'handle': 'edith', 'name': 'Evocative Edith'}
        response = self.client.post(self.server_url + '/users/', signup_data_missing_password)
        self.assertEqual(User.objects.count(), 4)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'password': ['This field is required.']}
        self.assertEqual(response.data, data)

        signup_data_missing_everything = {}
        response = self.client.post(self.server_url + '/users/', signup_data_missing_everything)
        self.assertEqual(User.objects.count(), 4)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'email': ['This field is required.'],
                'handle': ['This field is required.'],
                'name': ['This field is required.'],
                'password': ['This field is required.']}
        self.assertEqual(response.data, data)

    def test_no_one_can_create_a_user_with_bad_information(self):
        signup_data_broken_email = {'email': 'edith', 'password': 'ee', 'handle': 'edith', 'name': 'Evocative Edith'}
        response = self.client.post(self.server_url + '/users/', signup_data_broken_email)
        self.assertEqual(User.objects.count(), 4)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'email': ['Enter a valid email address.']}
        self.assertEqual(response.data, data)

    def test_anyone_can_access_a_specific_user(self):
        users = self.client.get(self.server_url + '/users/').data
        bob_url = users[1]['url']
        bob = self.client.get(bob_url)
        self.assertEqual(bob.status_code, status.HTTP_200_OK)
        self.assertEqual(bob.data['email'], 'bob@b.org')
        self.assertEqual(bob.data['handle'], 'bob')
        self.assertEqual(bob.data['name'], 'Bodacious Bob')
        self.assertEqual(bob.data['cheeps_count'], 0)
        self.assertEqual(bob.data['following_count'], 2)
        self.assertEqual(bob.data['followers_count'], 1)

    def test_no_one_can_access_user_passwords(self):
        users = self.client.get(self.server_url + '/users/').data
        first_user_url = users[0]['url']
        first_user = self.client.get(first_user_url)
        self.assertEqual(first_user.status_code, status.HTTP_200_OK)
        self.assertRaises(KeyError, lambda: first_user.data['password'])

    def test_anyone_can_access_all_cheeps(self):
        response = self.client.get(self.server_url + '/cheeps/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
