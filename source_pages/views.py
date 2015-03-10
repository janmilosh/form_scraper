from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from source_pages.models import SourcePage


# def index(request):
#     pages = SourcePage.objects.order_by('site_title')
#     output = ', '.join([p.site_title for p in pages])
#     return HttpResponse(output)

def detail(request, page_id):
    return HttpResponse("You're looking at page %s." % page_id)



def index(request):
    pages = SourcePage.objects.order_by('site_title')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'pages': pages,
    })
    return HttpResponse(template.render(context))