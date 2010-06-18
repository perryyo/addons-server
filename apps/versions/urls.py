from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns('',
    url('^$', views.version_list, name='addons.versions'),
    url('^(?P<version_id>\d+)$', views.version_detail,
        name='addons.versions'),
)
