import csv

from forms.models import Form, Hash


class HashComparer:
    def __init__(self):
        self.forms = Form.objects.exclude(ignore=True)
        self.run_index = 1


    def write_to_csv(self):
        # TODO: make file name/date dynamic
        with open('changed_forms_2015_05_23.csv', 'w') as f:
            writer = csv.writer(f)
            for index, form in enumerate(self.forms):
                if self._changed_hashes(form):
                    try:
                        writer.writerow([form.source_page, form.canonical_url, form.form_numbers])
                    except:
                        print form.status_code, form.source_page, form.canonical_url    

    def _changed_hashes(self, form):
        try:
            hashes = Hash.objects.filter(form_id=form.id)
            hash1 = hashes.get(last_run_index=self.run_index)
            hash2 = hashes.get(last_run_index=self.run_index-1)
            
            if hash1.sha256 != hash2.sha256:
                print form, 'Has changed.'
                return True
                             
        except BaseException, e:
            print
            print 'error', form.canonical_url
            print "error:", e
    

def run():
    form_hash = HashComparer()
    form_hash.write_to_csv()
