from rest_framework import status

from .base import RestClientTest


class CoreDataRestClientAccessTest(RestClientTest):

    def test_anyone_can_access_the_api(self):
        response = self.client.get(self.server_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anyone_can_access_all_users(self):
        response = self.client.get(self.server_url + '/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anyone_can_access_a_specific_user(self):
        response = self.client.get(self.server_url + '/users/2/')
        self.assertEqual(response.data['name'], 'Bodacious Bob')
        self.assertEqual(response.data['handle'], 'bob')
        self.assertEqual(response.data['cheeps_count'], 0)
        self.assertEqual(response.data['following_count'], 2)
        self.assertEqual(response.data['followers_count'], 1)
