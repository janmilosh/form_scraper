import sys
from queue import Queue
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
        this_run_index = 3
        forms = Form.objects.exclude(ignore=True).exclude(last_run_index=this_run_index)
        self.forms =list(forms) 
        random.shuffle(self.forms)
        print('Number of Forms:', len(self.forms))

        self.run_index = this_run_index
        self.count = 0


    def process_forms(self, forms):
        '''http://www.troyfawkes.com/learn-python-multithreading-queues-basics/'''
        def process_loop(form):
            while True:
                print(self.count)
                self.make_hash(form.get())
                form.task_done()
                self.count += 1

        q = Queue(maxsize=0)
        num_threads = 20
         
        for i in range(num_threads):
          worker = Thread(target=process_loop, args=(q,))
          worker.setDaemon(True)
          worker.start()
         
        for form in forms:
          q.put(form)
         
        q.join()


    def make_hash(self, form):
        # print(len(self.hashes))
        kwargs = {}
        hash = self._get_hash(form)
        if hash != False:
            kwargs['sha256'] = hash
            kwargs['form'] = form
            kwargs['last_run'] = timezone.now()
            kwargs['last_run_index'] = self.run_index
            h = Hash(**kwargs)
            print(kwargs['last_run'], hash, kwargs['last_run_index'])
            h.save()
        else:
            print("Hash not saved due to error")
  

    def _get_hash(self, form):
        try:               
            response = requests.get(form.canonical_url, timeout=30) 

            if response.ok:
                print('The response is ok:', response.ok)               
                print(response.status_code, form.canonical_url)
                form_hash = hashlib.sha256(response.content)
                sha256 =  form_hash.hexdigest()
                form.last_run_index = self.run_index
                form.status_code = response.status_code
                form.save()
                return sha256
            else:
                print("The response was not ok, code=", response.status_code)
                print(form.canonical_url)
                form.status_code = response.status_code
                form.save()
                return False
                                
        except:
            form.status_code = None
            form.save()
            print(form.canonical_url)
            print("Error:", str(sys.exc_info()[0]))
            return False 
       
 
def run():
    form_hash = FormHash()
    form_hash.process_forms(form_hash.forms)