from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^2/', views.index2, name='index2'),
    url(r'^concept/', views.concept, name='concept'),
    url(r'^concept2/', views.concept2, name='concep2'),
    url(r'^receiver/', views.receiver, name='receiver'),
    url(r'^async-joystick/', views.async_joystick, name='async_joystick'),
]