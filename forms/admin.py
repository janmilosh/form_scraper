from django.contrib import admin

from forms.models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'status_code', 'form_numbers', 'last_run_index', 'ignore',)
    search_fields = ['file_name', 'canonical_url']

admin.site.register(Form, FormAdmin)