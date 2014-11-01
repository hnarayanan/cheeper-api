from django.db import models

from custom_user.models import AbstractEmailUser


class User(AbstractEmailUser):
    """
    A simple model to hold our users.
    """

    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=25, unique=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, default='')
    is_following = models.ManyToManyField('self', related_name='has_followers',
                                          symmetrical=False, blank=True, null=True)

    def thumbnail_url(self):
        if self.thumbnail:
            return 'http://localhost:8000' + self.thumbnail.url
        return ''

    def cheeps_count(self):
        return self.cheeps.count()

    def following_count(self):
        return self.is_following.count()

    def followers_count(self):
        return self.has_followers.count()

    def stream(self):
        my_cheeps = self.cheeps.all()
        following = self.is_following.all()
        stream_cheeps = my_cheeps

        for person in following:
            stream_cheeps = stream_cheeps | person.cheeps.all()

        return stream_cheeps.order_by('-created')

    def __unicode__(self):
        return '%s' % self.name
