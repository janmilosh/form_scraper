# Form Scraper

A Django application for scraping and monitoring the status of pdf forms.

To run server:

```
$ python manage.py runserver
```

To start Python3 virtual environment:

```
$ workon form_scraper3
```

To backup database:

```
$ python manage.py dbbackup
```

To drop database:

```
$ dropdb formdata
```

To restore database from backup (clean start):

```
$ createdb formdata
$ psql formdata < db_2015_06_21.backup
```

To get commands on brew postgres:

```
$ brew info postgres
```

To run script that makes page requests (do this after new source pages are added to the database):

```
$ python manage.py runscript make_page_requests -v3
```

To run script that finds pdf forms on these pages and stores them in the database (do this periodically as new pdfs could be added to the source pages):

```
$ python manage.py runscript scrape_form_hrefs -v3
```

After scraping the forms, we need to get the hashes for this run (set run version in __init__):

```
$ python manage.py runscript make_hashes_threaded -v3
```

We need to filter out those forms that aren't of interest:

```
$ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args=check 'medicaremailorder'
```

To then filter out the forms and mark them as 'ignore' in the database: 

```
$ python manage.py runscript ignore_forms_by_keyword_or_status_code -v3 --script-args=save 'medicaremailorder'
```

Create a csv of the changed forms:

```
$ python manage.py runscript compare_hashes_and_write_to_csv -v3
```

Routes currently available:

All forms: ```http://localhost:8000/forms/```

Forms with status_codes other than 200 or 302: ```http://localhost:8000/pages/error_forms/```

All Source pages: ```http://localhost:8000/pages/```

Source pages with status_codes other than 200: ```http://localhost:8000/pages/error_pages/```