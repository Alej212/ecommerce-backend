from django.db import models
from djongo import models as djongo_models

class Shoe(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
    img = models.URLField()
    title = models.CharField(max_length=255)
    money = models.CharField(max_length=255)

    def __str__(self):
        return self.title

#img = models.ImageField(upload_to='productos/', null=True, blank=True)
#money = models.DecimalField(max_digits=6, decimal_places=2)
    
    # _id = djongo_models.ObjectIdField()
    # img = models.TextField(max_length=600)
    # title = models.TextField(max_length=200)
    # money = models.TextField(max_length=200) 