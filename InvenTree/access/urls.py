"""
URL lookup for Company app
"""


from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    url(r'new/?', views.GroupsCreateView.as_view(), name='group-create'),
    url(r'list/?', views.GroupsListView.as_view(), name='group-list'),

    

    # # url(r'orders/?', views.CompanyDetail.as_view(template_name='company/orders.html'), name='company-detail-orders'),

    # url(r'parts/?', views.CompanyDetail.as_view(template_name='company/detail_part.html'), name='company-detail-parts'),
    # url(r'stock/?', views.CompanyDetail.as_view(template_name='company/detail_stock.html'), name='company-detail-stock'),
    # url(r'purchase-orders/?', views.CompanyDetail.as_view(template_name='company/detail_purchase_orders.html'), name='company-detail-purchase-orders'),

    # url(r'thumbnail/?', views.CompanyImage.as_view(), name='company-image'),

    # # Any other URL
    # url(r'^.*$', views.CompanyDetail.as_view(), name='company-detail'),
]

