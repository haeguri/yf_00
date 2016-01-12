from django.conf.urls import url

urlpatterns = [
    url(r'^$',                         'shop.views.index',       name='index'),
    url(r'^item/(?P<item_id>[0-9]+)$', 'shop.views.item_detail', name='item_detail'),
    url(r'^item/new$',                 'shop.views.item_new',    name='item_new'),
]
