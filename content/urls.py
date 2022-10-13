from django.urls import path
from content import views

urlpatterns = [
    path('upload/', views.UploadFeed,name='upload'),
]
