from django.urls import path
from account import views


urlpatterns = [
    path('sign-up/', views.sign_up_view,name='sign-up'),
    path('sign-in/', views.sign_in_view,name='sign-in'),
]
