from django.urls import path
from . import views

urlpatterns = [
    path('', views.punto_list, name='punto_list'),
    path('delete/<int:pk>/', views.delete_punto, name='delete_punto'),
    path('detalle/<int:pk>/', views.punto_detail, name='punto_detail'),
]
