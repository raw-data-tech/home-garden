import urllib2

from django.shortcuts import get_object_or_404

from bs4 import BeautifulSoup
import Levenshtein as lev

from apps.vegetables.models import Vegetable

webpage = urllib2.urlopen('http://www.vfpck.org/mwiseprice.asp?ID=6')
soup = BeautifulSoup(webpage.read(), "html5")


def get_table():
    tables = list(soup.findAll('table'))
    return tables[1]


def get_trs(table):
    trs = table.findAll('tr')
    return trs[2:]


def get_tds(tr):
    output = []
    for tds in tr:
        for td in tds:
            value = td.strip()
            output.append(value)
    new_output = [x for x in output if len(x)]
    clean_data = []
    for item in new_output:
        try:
            clean_data.append(int(item))
        except:
            clean_data.append(item)
    return clean_data


def process():
    items = []
    table = get_table()
    trs = get_trs(table)
    for tr in trs:
        tds = get_tds(tr)
        items.append(tds)
    return items

# {
#     'name':
#     'retial':
#     price_wholesale
#     distance:
# }

def update_price():
    items = process()
    as_dict = to_dict(items)
    vegetables = Vegetable.objects.all()
    for v in vegetables:
        for d in as_dict:
            d['ratio'] = lev.ratio(v.name_en, d['name_en'])
        best_match = sorted(as_dict, key=lambda k: k['ratio'], reverse=True)[0]
        if best_match['ratio'] > .85:
            v.price_retail = best_match['price_retail']
            v.price_wholesale = best_match['price_wholesale']
            v.save()


def to_dict(items):
    dicts = []
    for item in items:
        item_dict = {
        'name_en': item[0],
        'price_wholesale': item[1],
        'price_retail': item[2]}
        dicts.append(item_dict)
    return dicts
