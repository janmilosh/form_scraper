from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from forms.models import Form


def index(request):
    forms = Form.objects.all()
    return render(request, 'forms/index.html',
            {'forms': forms,
             'number': len(forms)})

def has_etag(request):
    forms = Form.objects.exclude(current_etag = '')
    return render(request, 'forms/list_etags.html',
            {'forms': forms,
             'number': len(forms)})