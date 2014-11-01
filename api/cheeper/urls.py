from django.conf.urls import patterns, include, url

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserFollowingViewSet, UserFollowerViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
  url(r'^', include(router.urls)),
  url(r'^users/(?P<pk>[0-9]+)/following/$', UserFollowingViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-following'),
  url(r'^users/(?P<pk>[0-9]+)/following/(?P<followed>[0-9]+)/$', UserFollowingViewSet.as_view({'delete': 'destroy'}), name='user-following-destroy'),
  url(r'^users/(?P<pk>[0-9]+)/followers/$', UserFollowerViewSet.as_view({'get': 'list'}), name='user-followers'),
)
