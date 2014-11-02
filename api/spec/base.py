import sys

from rest_framework.test import APILiveServerTestCase

from users.models import User
from cheeps.models import Cheep

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

    def get_specific_user_url(self, id=0):
        users = self.client.get(self.server_url + '/users/')
        return users.data[id]['url']

    def setUp(self):
        alex = User.objects.create_user(email='alex@a.org', password='aa', name='Angry Alex', handle='alex')
        bob = User.objects.create_user(email='bob@b.org', password='bb', name='Bodacious Bob', handle='bob')
        cathy = User.objects.create_user(email='cathy@c.org', password='cc', name='Curious Catherine', handle='cathy')
        diana = User.objects.create_user(email='diana@d.org', password='dd', name='Delicious Diana', handle='diana')

        alex.is_following = [bob, cathy, diana]
        alex.save()
        bob.is_following = [alex, diana]
        bob.save()
        diana.is_following = [alex]
        diana.save()

    def tearDown(self):
        pass
