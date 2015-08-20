from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^main/$', 'main.views.arthur', name='arthur'),
    url(r'^movies/$', 'main.views.movies', name='movies'),
    # url(r'^crew/$', 'main.views.crew', name=crew),
    # url(r'cast/$', 'main.views.cast', name=cast),
]
