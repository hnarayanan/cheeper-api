from rest_framework import status

from cheeps.models import Cheep
from .base import RestClientTest


class CheepAccessTest(RestClientTest):

    def test_anyone_can_access_all_cheeps(self):
        response = self.client.get(self.server_url + '/cheeps/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_users_can_create_new_cheeps_with_content(self):
        self.client.login(email='cathy@c.org', password='cc')
        cheep_data = {'content': 'I guess I\'m late to the party'}
        response = self.client.post(self.server_url + '/cheeps/', cheep_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], cheep_data['content'])
        self.assertEqual(response.data['author']['handle'], 'cathy')
        self.client.logout()

    def test_users_cannot_create_new_cheeps_without_content(self):
        self.client.login(email='cathy@c.org', password='cc')
        cheep_data = {}
        response = self.client.post(self.server_url + '/cheeps/', cheep_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'content': ['This field is required.']}
        self.assertEqual(response.data, data)
        self.client.logout()

    def test_users_cannot_create_new_cheeps_with_content_over_140_characters_long(self):
        self.client.login(email='cathy@c.org', password='cc')
        cheep_data = {'content': 'This is too long a cheep to be accepted by the system. In fact, if it is accepted, we have a problem. Not a technical problem, but a social one where people when given the opportunity will likely blather on like I am now.'}
        response = self.client.post(self.server_url + '/cheeps/', cheep_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'content': ['Ensure this value has at most 140 characters (it has %d).' % len(cheep_data['content'])]}
        self.assertEqual(response.data, data)
        self.client.logout()

    def test_others_cannot_create_new_cheeps(self):
        cheep_data = {'content': 'I guess I\'m late to the party'}
        response = self.client.post(self.server_url + '/cheeps/', cheep_data)
        data = {'detail': 'Authentication credentials were not provided.'}
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, data)

    def test_anyone_can_access_a_specific_cheep(self):
        first_cheep = self.client.get(self.get_specific_cheep_url(9))
        self.assertEqual(first_cheep.status_code, status.HTTP_200_OK)
        self.assertEqual(first_cheep.data['content'], 'It was supposed to be called the Pod but Steve Jobs was still getting the hang of Vim.')
        self.assertEqual(first_cheep.data['author']['handle'], 'alex')

    def test_a_user_can_update_one_of_their_tweets(self):
        self.client.login(email='alex@a.org', password='aa')
        new_cheep_data = {'content': 'Perhaps this version is more boring.'}
        response = self.client.patch(self.get_specific_cheep_url(9), new_cheep_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], new_cheep_data['content'])
        self.client.logout()

    def test_no_one_else_can_update_a_users_tweets(self):
        # Anonymous requester
        new_cheep_data = {'content': 'Perhaps this version is more boring.'}
        response = self.client.patch(self.get_specific_cheep_url(9), new_cheep_data)
        data = {'detail': 'Authentication credentials were not provided.'}
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, data)
        # Another user
        self.client.login(email='bob@b.org', password='bb')
        response = self.client.patch(self.get_specific_cheep_url(9), new_cheep_data)
        data = {'detail': 'You do not have permission to perform this action.'}
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, data)
        self.client.logout()

    def test_a_user_can_delete_one_of_their_tweets(self):
        self.client.login(email='alex@a.org', password='aa')
        response = self.client.delete(self.get_specific_cheep_url(9))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

    def test_no_one_else_can_delete_a_users_tweets(self):
        # Anonymous requester
        response = self.client.delete(self.get_specific_cheep_url(9))
        data = {'detail': 'Authentication credentials were not provided.'}
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, data)
        # Another user
        self.client.login(email='bob@b.org', password='bb')
        response = self.client.delete(self.get_specific_cheep_url(9))
        data = {'detail': 'You do not have permission to perform this action.'}
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, data)
        self.client.logout()
