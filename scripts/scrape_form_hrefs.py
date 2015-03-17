from django.utils import timezone

from source_pages.models import SourcePage
from forms.models import Form
from helpers.pdf_scrape import Helpers


class PDFScraper:
    def __init__(self):
        self.pages = SourcePage.objects.filter(status_code__in=[200, 302])
        self.forms = Form.objects.all()
        self.helpers = Helpers()

    def scrape_pdfs(self):
        for page in self.pages:
            response = self.helpers.request_source_page(page.site_url)
            links = self.helpers.get_pdf_links_from_page_response(response)

            print page.site_url
            print page.site_title
            print links

            for link in links:
                form_name = self.helpers.create_form_name(link)
                canonical_url = self.helpers.create_canonical_url(page.site_url, link)
                print form_name
                print canonical_url
                self._save_pdf_to_database(page, form_name, canonical_url)

    def _save_pdf_to_database(self, page, form_name, canonical_url):
        '''Saves each pdf for the given page,
        but only if not already in the database.
        '''
        kwargs = {}
        kwargs['canonical_url'] = canonical_url
                
        if len(self.forms.filter(**kwargs)) == 0:
            kwargs['file_name'] = form_name
            kwargs['source_page'] = page
            kwargs['timestamp'] = timezone.now()
            f = Form(**kwargs)
            f.save()


def run():
    scraper = PDFScraper()
    scraper.scrape_pdfs()

