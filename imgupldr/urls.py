from django.contrib import admin
from django.conf.urls import url

from . import views

app_name = 'imgupldr'

urlpatterns = [
    url(r'^$', views.upload_pic, name='index'),
]
