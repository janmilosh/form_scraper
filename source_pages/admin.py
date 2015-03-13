from django.contrib import admin

from source_pages.models import SourcePage


class SourcePageAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'site_url', 'notes', 'status_code')
    search_fields = ['site_title']

admin.site.register(SourcePage, SourcePageAdmin)