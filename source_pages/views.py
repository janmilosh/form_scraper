from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from source_pages.models import SourcePage


def index(request):
    pages = SourcePage.objects.order_by('site_title')
    return render(request, 'index.html',
            {'pages': pages,
             'number': len(pages)})

def error_pages(request):
    error_pages = SourcePage.objects.order_by('status_code')
    ok_status_codes = [200, 302]
    for code in ok_status_codes:
        error_pages = error_pages.exclude(status_code=code)
    
    number = len(error_pages)
    return render(request, 'error_pages.html',
            {'error_pages': error_pages,
             'number': number})