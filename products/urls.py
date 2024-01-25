from django.urls import path
from . import views  

urlpatterns = [
    path('shoes/', views.ShoesList.as_view()),
    path('sweaters/', views.SweaterList.as_view()),
    path('jackets/', views.JacketList.as_view()),
    path('pants/', views.PantsList.as_view()),
    path('shoes/<str:custom_id>/', views.ShoesDetail.as_view()),
    path('sweaters/<str:custom_id>/', views.SweatersDetail.as_view()),
    path('jackets/<str:custom_id>/', views.JacketsDetail.as_view()),
    path('pants/<str:custom_id>/', views.PantsDetail.as_view()),
]
