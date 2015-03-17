from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from forms.models import Form


def index(request):
    forms = Form.objects.all()
    return render(request, 'forms/index.html',
            {'forms': forms,
             'number': len(forms)})