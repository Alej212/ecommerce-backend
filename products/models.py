from django.db import models
from djongo import models
from django.utils import timezone

class Products(models.Model):
    custom_id = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100, null=True)
    type_product = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True

class Shoes(Products):

    def __str__(self):
        return self.title
    
    class Meta: 
        db_table = 'shoes'

class Sweaters(Products):

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'sweaters'

class Jackets(Products):

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'jackets'

class Pants(Products):

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'pants'