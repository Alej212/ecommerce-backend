from django.db import models
from djongo import models as djongo_models

# En tu archivo models.py
from django.db import models

class Products(models.Model):
    image = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Shoes(Products):

    def __str__(self):
        return self.title
    
    class Meta: 
        db_table = 'shoes'

class Sweater(Products):

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'sweater'

class Jacket(Products):

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'jacket'

class Pants(Products):

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'pants'