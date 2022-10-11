from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainHome, name='MainHome'),
]
