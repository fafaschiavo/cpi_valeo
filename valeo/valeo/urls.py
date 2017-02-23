from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^vr/', include('vr.urls')),
    url(r'^admin/', admin.site.urls),
]