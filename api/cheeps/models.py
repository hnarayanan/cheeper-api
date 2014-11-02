from django.db import models

from users.models import User


class Cheep(models.Model):
    """
    A simple model to hold our cheeps.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name="cheeps")
    content = models.CharField(max_length=140)

    def __unicode__(self):
        return '%s: %s' % (self.author, self.content)

    class Meta:
        ordering = ('-modified',)
