from django.urls import path
from . import views

urlpatterns = [
    path('', views.free_kick_challenge, name='free_kick_challenge'),
]
