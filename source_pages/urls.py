from django.conf.urls import patterns, url

from source_pages import views

urlpatterns = patterns('',
    url(r'^get_pages/$', views.get_pages, name='get_pages'),
    # url(r'^page_errors/$', views.page_errors, name='page_errors'),
    # url(r'^(?P<page_id>\d+)/$', views.detail, name='detail'),
)

