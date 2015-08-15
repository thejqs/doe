from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    urls(r'^films/$', 'main.views.films', name=films),

]