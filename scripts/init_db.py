from django.db import transaction

from apps.account.models import User
from apps.vegetables.models import Vegetable


def get_line_arrays(file_name):
    file_name = '_temp/db/' + file_name
    with open(file_name) as f:
        content = f.readlines()
        return [line.strip().split(',') for line in content]

def _create_superuser():
    if User.objects.all():
        return
    print "creating super user..."
    user = User.objects.create_superuser(
        username='9886372343',
        email='admin@gmail.com',
        password='abcd1234',)
    return user


def _fill_vegetables():
    print "adding vegetables..."
    for i in get_line_arrays('vegetables.txt'):
        print i
        Vegetable.objects.create(
            name_en=i[0].strip(),
            name_ml=i[1].strip(),
            image_url=i[2].strip(),
        )
        

@transaction.atomic
def run():
    _create_superuser()
    _fill_vegetables()

