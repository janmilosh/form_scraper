from forms.models import Form, Hash

from django.utils import timezone

import hashlib
import requests


class FormHash:
    def __init__(self):
        # self.forms = Form.objects.exclude(ignore=True)
        self.hashes = Hash.objects.all()
        self.run_index = 1

    def make_hashes(self):
        print len(self.hashes)
        
        for index, form in enumerate(self.forms):

            kwargs = {}
            hash = self._get_hash(index, form)
            if hash != 'Error':
                kwargs['sha256'] = hash
                kwargs['form'] = form
                kwargs['last_run'] = timezone.now()
                kwargs['last_run_index'] = self.run_index
                h = Hash(**kwargs)
                print kwargs['last_run'], h, kwargs['last_run_index']
                h.save()
            else:
                print "Hash not saved due to error"

    def _get_hash(self, index, form):
        form.last_run_index = self.run_index
        try:               
            response = requests.get(form.canonical_url)                
            print index, response.status_code, form.canonical_url
            form_hash = hashlib.sha256(response.content)
            sha256 =  form_hash.hexdigest()
            form.status_code = response.status_code
            form.save()
            return sha256
                                
        except BaseException, e:
            '''Mark those with errors to ignore,
            but first do a dry run and see what they are.'''
            # form.ignore = True
            form.status_code = None
            form.save()
            print index, form.canonical_url
            print "Error:", e
            return 'Error'         


def run():
    form_hash = FormHash()
    form_hash.make_hashes()
