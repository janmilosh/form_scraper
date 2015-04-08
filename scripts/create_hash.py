import hashlib, requests, pdb, os

from forms.models import Form
from helpers.pdf_scrape import Helpers


class FormHash:
    def __init__(self):
        self.forms = Form.objects.all()[500:1000]

    def create_hash(self):
        for index, form in enumerate(self.forms):

            try:
                response = requests.get(form.canonical_url)
                
                if response.status_code == requests.codes.ok:
                    print index, form.canonical_url
                    form_hash = hashlib.sha256(response.content)
                    form.current_sha256 =  form_hash.hexdigest()
                    form.status_code = response.status_code
                    form.save()
                    print form.status_code, form.current_sha256
                    

            except:
                print "There was a problem with the form:"
                print index, form.canonical_url            


def run():
    form_hash = FormHash()
    form_hash.create_hash()
