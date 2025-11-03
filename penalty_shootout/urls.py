from django.urls import path
from . import views

urlpatterns = [
    path('', views.penalty_shootout, name='penalty_shootout'),
]
