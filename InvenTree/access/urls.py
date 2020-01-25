"""
URL lookup for Company app
"""


from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    url(r'new/?', views.GroupsCreateView.as_view(), name='group-create'),
    url(r'update/?', views.GroupUpdateView.as_view(), name='group-update'),
    url(r'delete/?', views.GroupsDeleteView.as_view(), name='group-delete'),
    url(r'list/?', views.GroupsListView.as_view(), name='group-list'),
]

