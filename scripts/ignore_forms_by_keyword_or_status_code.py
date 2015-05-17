import pdb

from forms.models import Form


class Ignorer:

    '''This class contains the method for finding
    forms to ignore based on a keyword in the
    canonical url.
    '''

    def __init__(self):
        self.forms = Form.objects.exclude(ignore=True)

    def ignore_forms_with_keywords(self, keywords):
        count = 0
        for form in self.forms:
            for word in keywords:
                if word.lower() in form.canonical_url.lower():
                    count += 1
                    form.ignore = True
                    form.save()
                    print(count, form.canonical_url)

    def ignore_404s(self):
        count = 0
        status_codes = (300, 401, 404)
        # add 403's to these status codes once new, fixed versions of
        # the urls have been added to the database.
        for form in self.forms:
            for status_code in status_codes:
                if form.status_code == status_code:
                    count += 1
                    form.ignore = True
                    form.save()
                    print(count, form.status_code, form.canonical_url)
                    
def run():
    keywords = ('rationale',
                'BlueSaludFormularyUpdates',
                'mmp_formulary',
                'classic_formulary',
                'eg_formulary',
                'jade_formulary',
                'benefit-limit-exception',
                'MCP_Formulary_508',
                'AlpCarHydCombo.pdf',
                'Medicaid_News',
                'web_announcement',
                'non_claim_remit_cost_share',
                'provider_taxonomy_guide',
                'benefit chart',
                'druglist',
                'prescription drug tiers',
                '4b7026a5beff4156bfedc051f486e81b',
                'a510490e06f14f3fab558b9def64a063',
                '827712a15b2545659f88ef3c0a121d31',
                'ca5ad75a759d42f29c917bae2fd5539f',
                'pa-guidelines',
                'pw_e210962',
                'pw_e210963',
                'Publications',
                'Transportation',
                'coordination',
                'administrative',
                'billing',
                'notification',
                'immunization',
                'hysterectomy',
                'behavioral',
                'behavorial',
                'admission',
                'data',
                'disclosure',
                'psychosocial',
                'instructions',
                'outpatient',
                'codification',
                '40-460',
                'provider_appeal',
                'authorization_list',
                'application_to',
                'ancillary',
                'news',


                )
    ignorer = Ignorer()
    ignorer.ignore_forms_with_keywords(keywords)
    ignorer.ignore_404s()