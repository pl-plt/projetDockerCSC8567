from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('form/', views.formulaireNom ),
    path('success/', views.success ),
]