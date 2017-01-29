"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
  #  Inside apps/first_app/views.py
from django.shortcuts import render, HttpResponse
  # While Django will automatically create the request object for us that's passed into our method, HttpResponse objects are our responsibility to create and return to the browser.
  #  Note that 'render' is a shortcut method that combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
  # Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
    # Not using render because we haven't created any templates yet!
