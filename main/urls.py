from django.urls import path
from main.views import MainHome

urlpatterns = [
    path('', MainHome, name='main_home')
]
