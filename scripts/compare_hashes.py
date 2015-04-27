from django.utils import timezone
import hashlib, requests, pdb, os

from forms.models import Form
from helpers.pdf_scrape import Helpers


class FormHash:
    def __init__(self):
        self.forms = Form.objects.exclude(current_sha256='', ignore=True)

    def create_hash(self):
        for index, form in enumerate(self.forms[0:1000]):
            # print index, form.canonical_url
            try:
                response = requests.get(form.canonical_url)                
                form_hash = hashlib.sha256(response.content)
                form.new_sha256 =  form_hash.hexdigest()
                form.status_code = response.status_code
                form.last_run = timezone.now()
                print index
                if form.current_sha256 != form.new_sha256:
                    print index, form.status_code, form.canonical_url
                                    
            except BaseException, e:
                print index, form.canonical_url
                print "Error:", e            


def run():
    form_hash = FormHash()
    form_hash.create_hash()
