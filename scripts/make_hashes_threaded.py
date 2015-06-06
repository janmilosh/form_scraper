import hashlib, random, threading
import requests

from django.utils import timezone

from forms.models import Form, Hash


class FormHash:
    def __init__(self):
        '''Form objects must be put into a list so that
        they can be randomized.
        '''
        self.forms = Form.objects.exclude(ignore=True)[700:710]
        # self.hashes = Hash.objects.all()
        self.run_index = 2


    def make_hash(self, form):
        # print len(self.hashes)
        print form.canonical_url
        kwargs = {}
        hash = self._get_hash(form)
        if hash != 'Error':
            kwargs['sha256'] = hash
            kwargs['form'] = form
            kwargs['last_run'] = timezone.now()
            kwargs['last_run_index'] = self.run_index
            h = Hash(**kwargs)
            print kwargs['last_run'], h, kwargs['last_run_index']
            # h.save()
        else:
            print "Hash not saved due to error"
  

    def _get_hash(self, form):
        form.last_run_index = self.run_index
        try:               
            response = requests.get(form.canonical_url)                
            print response.status_code, form.canonical_url
            form_hash = hashlib.sha256(response.content)
            sha256 =  form_hash.hexdigest()
            form.status_code = response.status_code
            # form.save()
            return sha256
                                
        except BaseException, e:
            '''Mark those with errors to ignore,
            but first do a dry run and see what they are.'''
            # form.ignore = True
            form.status_code = None
            # form.save()
            print form.canonical_url
            print "Error:", e
            return 'Error'         


def run(poolsize):
    form_hash = FormHash()

    '''Get the forms and randomize them.'''
    forms = list(form_hash.forms)
    random.shuffle(forms)
    
    '''Make the requests and hashes concurrently'''

    pool = ThreadPool(int(poolsize))
    requests = makeRequests(form_hash.make_hash, forms)
    [pool.putRequest(req) for req in requests]
    pool.wait()

    p.map(form_hash.make_hash, forms)

    
