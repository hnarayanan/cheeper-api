from rest_framework import status

from cheeps.models import Cheep
from .base import RestClientTest


class CheepAccessTest(RestClientTest):

    def test_anyone_can_access_all_cheeps(self):
        response = self.client.get(self.server_url + '/cheeps/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_users_can_create_new_cheeps(self):
        self.client.login(email='cathy@c.org', password='cc')
        cheep_data = {'content': 'I guess I\'m late to the party'}
        response = self.client.post(self.server_url + '/cheeps/', cheep_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], cheep_data['content'])
        self.assertEqual(response.data['author']['handle'], 'cathy')
        self.client.logout()

    def test_others_cannot_create_new_cheeps(self):
        cheep_data = {'content': 'I guess I\'m late to the party'}
        response = self.client.post(self.server_url + '/cheeps/', cheep_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
