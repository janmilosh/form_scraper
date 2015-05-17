from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from forms.models import Form


def index(request):
    forms = Form.objects.exclude(ignore=True)
    return render(request, 'forms/index.html',
            {'forms': forms,
             'number': len(forms)})

def has_etag(request):
    forms = Form.objects.exclude(current_etag = '')
    return render(request, 'forms/list_etags.html',
            {'forms': forms,
             'number': len(forms)})

def error_forms(request):
    error_forms = Form.objects.order_by('status_code')
    ok_status_codes = [200, 302]
    for code in ok_status_codes:
        error_forms = error_forms.exclude(status_code=code)
    
    number = len(error_forms)
    return render(request, 'forms/error_forms.html',
            {'error_forms': error_forms,
             'number': number})