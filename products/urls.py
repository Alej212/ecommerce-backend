from django.urls import path
from . import views  # Asegúrate de importar tus vistas

urlpatterns = [
    path('check-connection/', views.check_connection, name='check_connection'),
    path('list-products/', views.ShoeList.as_view(), name='product-list'),
]
