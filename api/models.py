from django.db import models
from djongo import models as djongo_models

# En tu archivo models.py
from django.db import models

class Products(models.Model):
    _id = models.CharField(max_length=24)
    image = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100, null=True)
    type_product = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

class Shoes(Products):

    def save(self, *args, **kwargs):
        self.type_product = 'shoes'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta: 
        db_table = 'shoes'

class Sweater(Products):

    def save(self, *args, **kwargs):
        self.type_product = 'sweater'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'sweater'

class Jacket(Products):

    def save(self, *args, **kwargs):
        self.type_product = 'jacket'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'jacket'

class Pants(Products):


    def save(self, *args, **kwargs):
        self.type_product = 'pants'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'pants'