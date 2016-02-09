from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', name='login', kwargs={'template_name': 'login.html'}),
    url(r'^accounts/logout/','django.contrib.auth.views.logout',name='logout'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
