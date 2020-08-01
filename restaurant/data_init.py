import csv
import os, sys
import django

os.chdir(".")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant.settings")
django.setup()

from store.models import *

# stores
CSV_PATH = './csv/stores.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        Store.objects.create(
            name = row['name'],
            description = row['description'],
            address = row['address'],
            phone_number = row['phone_number']
        )

# menus
CSV_PATH = './csv/menus.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        Menu.objects.create(
            store_id = Store.objects.get(id=row['store_id']),
            name = row['name'],
            price = row['price']
        )
