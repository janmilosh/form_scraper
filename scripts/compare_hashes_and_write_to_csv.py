import csv

from forms.models import Form, Hash


class HashComparer:
    def __init__(self):
        self.forms = Form.objects.exclude(ignore=True)
        self.run_index = 2


    def write_to_csv(self):
        # TODO: make file name/date dynamic
        with open('new_and_changed_forms_2015_06_07.csv', 'w') as f:
            writer = csv.writer(f)
            for index, form in enumerate(self.forms):
                result, message = self._evaluate_hashes(form)
                if result:
                    try:
                        writer.writerow([form.source_page, form.canonical_url, message, form.form_numbers])
                    except:
                        print form.status_code, form.source_page, form.canonical_url    


    def _evaluate_hashes(self, form):
        try:
            hashes = Hash.objects.filter(form_id=form.id)
            current_hash_queryset = hashes.filter(last_run_index=self.run_index)
            previous_hash_queryset = hashes.filter(last_run_index=self.run_index-1)
            
            if len(previous_hash_queryset) == 0:
                print 'This is a new form', form.canonical_url
                return True, 'New'

            else:
                current_hash = current_hash_queryset[0]
                previous_hash = previous_hash_queryset[0]
                if current_hash.sha256 != previous_hash.sha256:
                    print form, 'Has changed.'
                    return True, 'Changed'
                return False, 'No Change'
                             
        except BaseException, e:
            print '*' * 60
            print 'error', form.canonical_url
            print 'error:', e
            print '*' * 60
    

def run():
    form_hash = HashComparer()
    form_hash.write_to_csv()
