from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from source_pages.models import SourcePage


def detail(request, page_id):
    return HttpResponse("You're looking at page %s." % page_id)

def index(request):
    pages = SourcePage.objects.order_by('site_title')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'pages': pages,
    })
    return HttpResponse(template.render(context))

def update_page_request_data():
    pages = SourcePage.objects.all()
    for page in pages:
        response = page.request_source_page()
        page.status_code = response['status_code']
        page.error_message = response['error_message']
        page.save()

def get_pages(request):
    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    if(request.GET.get('start_requests')):
        
        update_page_request_data()
    template = loader.get_template('request_pages.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))



