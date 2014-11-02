import sys

from django.core.urlresolvers import reverse

from rest_framework.test import APILiveServerTestCase


class RestClientTest(APILiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        APILiveServerTestCase.setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
           APILiveServerTestCase.tearDownClass()

    def endpoint(self, resource=''):
        base_path = '/v1/'
        endpoint = self.server_url + base_path
        if resource != '':
            endpoint = endpoint + resource + '/'
        return endpoint

    def setUp(self):
        # Setup users and cheeps here
        pass


    def tearDown(self):
        pass
