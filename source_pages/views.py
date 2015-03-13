from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from source_pages.models import SourcePage
from source_pages.scrape.source import PageRequests


def index(request):
    pages = SourcePage.objects.order_by('site_title')
    return render(request, 'index.html',
            {'pages': pages,
             'number': len(pages)})

def get_pages(request):
    page_requests = PageRequests()
    if(request.GET.get('start_requests')):
        page_requests.update_page_request_data()
        return render(request, 'request_pages.html')

def error_pages(request):
    error_pages = SourcePage.objects.exclude(status_code=200)
    number = len(error_pages)
    return render(request, 'error_pages.html',
            {'error_pages': error_pages,
             'number': number})