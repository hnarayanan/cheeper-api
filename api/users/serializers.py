from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    avatar_url = serializers.CharField(source='avatar_url', read_only=True)
    cheeps_count = serializers.CharField(source='cheeps_count', read_only=True)
    cheeps_url = serializers.HyperlinkedIdentityField(view_name='user-cheeps')
    following_count = serializers.CharField(source='following_count', read_only=True)
    following_url = serializers.HyperlinkedIdentityField(view_name='user-following')
    followers_count = serializers.CharField(source='followers_count', read_only=True)
    followers_url = serializers.HyperlinkedIdentityField(view_name='user-followers')
    stream_url = serializers.HyperlinkedIdentityField(view_name='user-stream')

    class Meta:
        model = User
        fields = ('id', 'url', 'email', 'password', 'name', 'handle',
                  'avatar', 'avatar_url', 'cheeps_count',
                  'cheeps_url', 'following_count', 'following_url',
                  'followers_count', 'followers_url', 'stream_url')
        write_only_fields = ('avatar', 'password')


class CheepAuthorSerializer(serializers.HyperlinkedModelSerializer):

    avatar_url = serializers.CharField(source='avatar_url', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'name', 'handle', 'avatar_url')
