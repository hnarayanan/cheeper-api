from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from users.models import User
from .models import Cheep
from .serializers import CheepSerializer
from .permissions import IsAuthorOrReadOnly


class CheepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cheeps to be viewed or edited.
    """
    queryset = Cheep.objects.all()
    serializer_class = CheepSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user


class UserCheepViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieves cheeps by a given author.
    """
    def list(self, request, pk=None):
       author = get_object_or_404(User, pk=pk)
       cheeps = author.cheeps.all()
       serializer = CheepSerializer(cheeps, many=True)
       return Response(serializer.data)


class UserStreamViewSet(viewsets.ViewSet):
    """
    API endpoint that retrieves a user's stream. That's a list of all
    the cheeps that they've authored along with those of the users
    that they follow.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)

    def list(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        cheeps = user.stream()
        serializer = CheepSerializer(cheeps, many=True)
        return Response(serializer.data)
