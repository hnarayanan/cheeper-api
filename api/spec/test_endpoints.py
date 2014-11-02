from rest_framework import status

from .base import RestClientTest


class CoreDataRestClientAccessTest(RestClientTest):

    def test_anyone_can_access_the_api(self):

        response = self.client.get(self.server_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {'cheeps': 'http://testserver/cheeps/', 'users': 'http://testserver/users/'}
        self.assertEqual(response.data, data)
