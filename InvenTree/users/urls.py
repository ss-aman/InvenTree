from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserModelViewSet)


user_urls = [
    url(r'token', views.GetAuthToken.as_view(), name='api-token'),

    url(r'^users/', views.UserListView.as_view(), name='user-list'),
    url(r'^create-user/', views.CreateUserView.as_view(), name='create-user'),
    url(r'^update-user/(?P<pk>[0-9]+)/', views.UpdateUserView.as_view(), name='update-user'),

    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.AccountActivationView.as_view(), name='acount-activate'),
]
user_urls += router.urls
