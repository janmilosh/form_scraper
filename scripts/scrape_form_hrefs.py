from source_pages.models import SourcePage
from forms.models import Form
from helpers.pdf_scrape import Helpers


class PDFScraper:
    def __init__(self):
        self.pages = SourcePage.objects.filter(status_code=200)
        self.helpers = Helpers()

    def scrape_pdfs(self):
        for page in self.pages[3:4]:
            response = self.helpers.request_forms_page(page.site_url)
            links = self._get_pdf_links_from_page_response(response)

            print page.site_url
            print page.site_title
            print links

            for link in links:
                form_name = self.helpers.create_form_name(link)
                print form_name
            
    def _get_pdf_links_from_page_response(self, response):
        soup = self.helpers.make_soup(response.text)
        forms = self.helpers.return_only_pdf_links(soup)
        return forms
    

def run():
    scraper = PDFScraper()
    scraper.scrape_pdfs()

