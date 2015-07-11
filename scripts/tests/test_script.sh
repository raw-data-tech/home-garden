python manage.py test  --settings=settings.dev
coverage run manage.py test --settings=settings.dev
coverage html
firefox htmlcov/index.html
