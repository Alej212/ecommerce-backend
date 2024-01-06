from django.urls import path
from . import views  

urlpatterns = [
    path('', views.ShoesList.as_view()),
]
