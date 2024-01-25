from django.contrib import admin
from .models import Shoes, Sweaters, Jackets, Pants

# Registra tus modelos aquí
admin.site.register(Shoes)
admin.site.register(Sweaters)
admin.site.register(Jackets)
admin.site.register(Pants)