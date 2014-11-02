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

    def get_specific_cheep_url(self, id=0):
        cheeps = self.client.get(self.server_url + '/cheeps/')
        return cheeps.data[id]['url']

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

        Cheep.objects.create(author=alex, content='It was supposed to be called the Pod but Steve Jobs was still getting the hang of Vim.')
        Cheep.objects.create(author=bob, content='Hi! I\'m Bob!')
        Cheep.objects.create(author=bob, content='What\'s going on?')
        Cheep.objects.create(author=alex, content='Raisin cookies that look like chocolate chip cookies are the main reason I have trust issues.')
        Cheep.objects.create(author=diana, content='This is my first post.')
        Cheep.objects.create(author=alex, content='#1: Advice for a daughter depends almost entirely on how attractive she is.')
        Cheep.objects.create(author=alex, content='Always keep your skills sharp. Or, as Jay-Z might say, "Ya slackin on your pimpin, turn it up."')
        Cheep.objects.create(author=diana, content='This is my first second!')
        Cheep.objects.create(author=alex, content='I am basically just refreshing websites until I fucking die I guess.')
        Cheep.objects.create(author=bob, content='Hello, is this thing on?')


    def tearDown(self):
        pass
