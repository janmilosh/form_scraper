# Form Scraper

A Django application for scraping and monitoring the status of pdf forms.

To run server:

```
$ python manage.py runserver
```

To run script that makes page requests (do this after new source pages are added to the database):

```
$ python manage.py runscript make_page_requests -v3
```

To run script that finds pdf forms on these pages and stores them in the database (do this periodically as new pdfs could be added to the source pages):

```
$ python manage.py runscript scrape_form_hrefs -v3
```

After scraping the forms, we need to get the initial hashes and status codes:

```
$ python manage.py runscript create_hash -v3
```

We need to filter out those forms that aren't of interest:

```
$ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args='medicaremailorder'
```

To then filter out the forms and mark them as 'ignore' in the database: 

```
$ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args='medicaremailorder' s
```

This is a good time to create a csv of the forms that have just been added to the database:

```
$ python manage.py runscript write_new_form_urls_to_csv -v3
```

Periodically, we need to check to see which forms have changed:

```
$ python manage.py runscript compare_hashes -v3
```

Create a csv of the changed forms:

```
$ python manage.py runscript write_changed_hashes_to_csv -v3
```

Routes currently available:

All forms: ```http://localhost:8000/forms/```

Forms with status_codes other than 200 or 302: ```http://localhost:8000/pages/error_forms/```

All Source pages: ```http://localhost:8000/pages/```

Source pages with status_codes other than 200: ```http://localhost:8000/pages/error_pages/```