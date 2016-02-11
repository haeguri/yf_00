from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^item/(?P<item_id>[0-9]+)$', 'shop.views.item_detail', name='item_detail'),
    url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
]