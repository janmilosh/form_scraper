from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^pages/', include('source_pages.urls')),
    url(r'^forms/', include('forms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)