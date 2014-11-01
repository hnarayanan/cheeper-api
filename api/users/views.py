from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .permissions import IsUserOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly,)


class UserFollowingViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieves the list of users that a given user is
    following.
    """
    # TODO: Fix permissions for the following endpoints.

    def list(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        following = user.is_following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        followed = request.POST.get('user')
        followed_user = get_object_or_404(User, pk=followed)
        if followed_user not in user.is_following.all():
            user.is_following.add(followed_user)

        following = user.is_following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None, followed=None):
        user = get_object_or_404(User, pk=pk)
        followed_user = get_object_or_404(User, pk=followed)
        if followed_user in user.is_following.all():
            user.is_following.remove(followed_user)
        following = user.is_following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)


class UserFollowerViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieves the list of users a that are following
    a given user.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, pk=None):
       user = get_object_or_404(User, pk=pk)
       followers = user.has_followers.all()
       serializer = UserSerializer(followers, many=True)
       return Response(serializer.data)
