from django.urls import path
from . import views

urlpatterns = [
    path('', views.keeper_reflex, name='keeper_reflex'),
]
