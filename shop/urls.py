from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'shop.views.index', name='index'),
]
