from django.urls import path
from . import views  

urlpatterns = [
    path('apilist/', views.ShoesList.as_view(), name='product-list'),
]
