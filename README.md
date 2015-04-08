# Form Scraper

A Django application for scraping and monitoring the status of pdf forms.

To run server:

```
$ python manage.py runserver
```

To run script that makes page requests:

```
$ python manage.py runscript make_page_requests -v3
```

To run script that finds pdf forms on these pages and stores them in the database:

```
$ python manage.py runscript scrape_form_hrefs -v3
```

All forms: ```http://localhost:8000/forms/```

Forms that have Etags: ```http://localhost:8000/forms/has_etag/```

All Source pages: ```http://localhost:8000/pages/```

Source pages with status_codes other than 200: ```http://localhost:8000/pages/error_pages/```