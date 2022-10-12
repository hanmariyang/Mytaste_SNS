from django.urls import path
from main import views

urlpatterns = [
    path('', views.MainHome, name='main_home')
]
