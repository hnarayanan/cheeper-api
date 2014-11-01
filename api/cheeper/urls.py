from django.conf import settings
from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserFollowingViewSet, UserFollowerViewSet
from cheeps.views import CheepViewSet, UserCheepViewSet, UserStreamViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cheeps', CheepViewSet)

urlpatterns = patterns('',
  url(r'^', include(router.urls)),
  url(r'^users/(?P<pk>[0-9]+)/cheeps/$', UserCheepViewSet.as_view({'get': 'list'}), name='user-cheeps'),
  url(r'^users/(?P<pk>[0-9]+)/following/$', UserFollowingViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-following'),
  url(r'^users/(?P<pk>[0-9]+)/following/(?P<followed>[0-9]+)/$', UserFollowingViewSet.as_view({'delete': 'destroy'}), name='user-following-destroy'),
  url(r'^users/(?P<pk>[0-9]+)/followers/$', UserFollowerViewSet.as_view({'get': 'list'}), name='user-followers'),
  url(r'^users/(?P<pk>[0-9]+)/stream/$', UserStreamViewSet.as_view({'get': 'list'}), name='user-stream'),
)
