from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^login$', views.login),
    url(r'^login/login$', views.login_login),
    url(r'^register$', views.register),
    url(r'^register/create$', views.register_create),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/admin$', views.dashboard_admin),
    url(r'^dashboard/delete/(?P<id>\d+)$', views.user_delete),


]
