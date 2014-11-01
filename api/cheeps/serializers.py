from rest_framework import serializers

from users.serializers import CheepAuthorSerializer
from .models import Cheep


class CheepSerializer(serializers.HyperlinkedModelSerializer):

    author = CheepAuthorSerializer(read_only=True)

    class Meta:
        model = Cheep
        fields = ('id', 'url', 'created', 'modified', 'author', 'content')
