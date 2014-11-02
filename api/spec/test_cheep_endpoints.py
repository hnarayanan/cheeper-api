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
