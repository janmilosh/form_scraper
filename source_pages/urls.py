from django.conf.urls import patterns, url

from source_pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^error_pages/$', views.error_pages, name='error_pages'),
    # url(r'^(?P<page_id>\d+)/$', views.detail, name='detail'),
)
