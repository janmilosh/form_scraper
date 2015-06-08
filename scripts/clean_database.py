from forms.models import Form, Hash

class CleanDB:
    def __init__(self):
        self.hashes = Hash.objects.filter(last_run_index=2)
        self.forms = Form.objects.filter(last_run_index=2)
        print 'Number of forms:', len(self.forms)
        print 'Number of hashes:', len(self.hashes)


    def clean_hashes(self):
        for hash in self.hashes:
            print hash.last_run_index
            print hash.form_id
            hash.delete()
        print len(self.hashes)

    def clean_forms(self):
        for form in self.forms:
            print form.canonical_url
            form.last_run_index = 1
            form.save()


def run():
    clean_db = CleanDB()
    # clean_db.clean_hashes()
    # clean_db.clean_forms()