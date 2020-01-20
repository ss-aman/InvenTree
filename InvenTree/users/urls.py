from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserModelViewSet)


user_urls = [
    url(r'token', views.GetAuthToken.as_view(), name='api-token'),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.AccountActivationView.as_view(), name='acount-activate'),
    url(r'test', views.CheckPermissions.as_view(), name='api-token'),

]
user_urls += router.urls
