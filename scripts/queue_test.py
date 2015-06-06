from Queue import Queue
from threading import Thread
import hashlib, random
import requests

from django.utils import timezone

from forms.models import Form, Hash


class FormHash:
    def __init__(self):
        '''Form objects must be put into a list so that
        they can be randomized.
        '''
        self.forms = list(Form.objects.exclude(ignore=True)[100:110])
        random.shuffle(self.forms)
        # self.hashes = Hash.objects.all()
        self.run_index = 2
        self.count = 0

    def process_forms(self, forms):
        '''http://www.troyfawkes.com/learn-python-multithreading-queues-basics/'''
        def process_loop(form):
            while True:
                print self.count
                self.make_hash(form.get())
                form.task_done()
                self.count += 1

        q = Queue(maxsize=0)
        num_threads = 5
         
        for i in range(num_threads):
          worker = Thread(target=process_loop, args=(q,))
          worker.setDaemon(True)
          worker.start()
         
        for form in forms:
          q.put(form)
         
        q.join()


    def make_hash(self, form):
        # print len(self.hashes)
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
       
 
def run():
    form_hash = FormHash()
    form_hash.process_forms(form_hash.forms)