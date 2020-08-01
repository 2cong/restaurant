from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'stores'

class Menu(models.Model):
    store_id = models.ForeignKey('Store', on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = 'menus'
