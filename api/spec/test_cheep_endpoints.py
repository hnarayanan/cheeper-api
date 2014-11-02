from rest_framework import status

from cheeps.models import Cheep
from .base import RestClientTest


class CheepAccessTest(RestClientTest):

    def test_anyone_can_access_all_cheeps(self):
        response = self.client.get(self.server_url + '/cheeps/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
