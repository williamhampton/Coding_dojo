from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^sucess$', views.sucess),
    url(r'^remove/(?P<id>\d+)$', views.remove)
]
