from django.urls import path
from . import views  

urlpatterns = [
    path('shoes/', views.ShoesList.as_view()),
    path('sweaters/', views.SweaterList.as_view()),
    path('jackets/', views.JacketList.as_view()),
    path('pants/', views.PantsList.as_view()),
]
