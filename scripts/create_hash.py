import hashlib, requests, pdb, os

from forms.models import Form
from helpers.pdf_scrape import Helpers


class FormHash:
    def __init__(self):
        self.forms = Form.objects.filter(ignore=False)
        self.forms = Form.objects.filter(current_sha256='')
        
    def create_hash(self):
        print 'number of forms with no hash', len(self.forms)
        for index, form in enumerate(self.forms):
            # print index, form.canonical_url
            try:
                response = requests.get(form.canonical_url)                
                print index, form.status_code, form.canonical_url
                form_hash = hashlib.sha256(response.content)
                form.current_sha256 =  form_hash.hexdigest()
                form.status_code = response.status_code
                form.save()
                print form.current_sha256
                                    
            except BaseException, e:
                print index, form.canonical_url
                print "Error:", e            


def run():
    form_hash = FormHash()
    form_hash.create_hash()
