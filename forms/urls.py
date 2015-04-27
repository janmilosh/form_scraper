from django.conf.urls import patterns, url

from forms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^has_etag/$', views.has_etag, name='has_etag'),
    url(r'^error_forms/$', views.error_forms, name='error_forms'),
    # url(r'^(?P<page_id>\d+)/$', views.detail, name='detail'),
)
