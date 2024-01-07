from django.db import models
from djongo import models as djongo_models

# En tu archivo models.py
from django.db import models

class Shoes(models.Model):
    image = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    
    class Meta: 
        db_table = 'shoes'

#image = models.ImageField(upload_to='media/shoes/', null=True, blank=True)
