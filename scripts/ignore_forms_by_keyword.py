import pdb

from forms.models import Form


class Ignorer:

    '''This class contains the method for finding
    forms to ignore based on a keyword in the
    canonical url.
    '''

    def __init__(self):
        self.forms = Form.objects.exclude(ignore=True)

    def ignore_forms(self, keywords):
        count = 0
        for form in self.forms:
            for word in keywords:
                if word.lower() in form.canonical_url.lower():
                    count += 1
                    form.ignore = True
                    # form.save()
                    print(count, form.canonical_url)
                    
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


                )
    ignorer = Ignorer()
    ignorer.ignore_forms(keywords)