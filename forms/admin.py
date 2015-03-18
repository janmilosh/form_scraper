from django.contrib import admin

from forms.models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'status_code', 'last_modified', 'current_etag')
    search_fields = ['file_name', 'canonical_url']

admin.site.register(Form, FormAdmin)