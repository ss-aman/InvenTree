from django.conf.urls import url

from . import views

user_urls = [
    url(r'^(?P<pk>[0-9]+)/?$', views.UserDetail.as_view(), name='user-detail'),
    url(r'token', views.GetAuthToken.as_view(), name='api-token'),

    url(r'^$', views.UserList.as_view()),

    url(r'^users/', views.UserListView.as_view(), name='user-list'),
    url(r'^create-user/', views.CreateUserView.as_view(), name='create-user'),
    url(r'^update-user/(?P<pk>[0-9]+)/', views.UpdateUserView.as_view(), name='update-user'),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.AccountActivationView.as_view(), name='acount-activate')
]
