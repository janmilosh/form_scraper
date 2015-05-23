from django.utils import timezone
import hashlib, requests, pdb, os

from forms.models import Form
from helpers.pdf_scrape import Helpers


class FormHash:
    def __init__(self):
        self.forms = Form.objects.exclude(current_sha256='', ignore=True)

    def create_hash(self):
        for index, form in enumerate(self.forms[15000:]):
            try:
                response = requests.get(form.canonical_url)            
                form_hash = hashlib.sha256(response.content)
                form.previous_sha256 = form.current_sha256
                form.current_sha256 = form_hash.hexdigest()
                form.status_code = response.status_code
                form.last_run = timezone.now()
                print index
                if form.current_sha256 != form.previous_sha256:
                    print 'change', index, form.canonical_url
                    print 'change', form.status_code, form.current_sha256, form.previous_sha256 
                else:
                    print 
                    print 'no change', index, form.canonical_url
                    print 'no change', form.status_code, form.current_sha256, form.previous_sha256 
                                    
            except BaseException, e:
                print
                print 'error', index, form.canonical_url
                print "error:", e
                form.notes = e

            form.save()
       

def run():
    form_hash = FormHash()
    form_hash.create_hash()
