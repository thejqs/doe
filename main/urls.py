from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', 'main.views.arthur', name='arthur'),
    url(r'^movies/$', 'main.views.movies', name='movies'),
    url(r'^crew/$', 'main.views.crew', name='crew'),
    url(r'^cast/$', 'main.views.cast', name='cast'),
    # url(r'^warhol/$', 'main.views.warhol', name='warhol')
]
