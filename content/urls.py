from django.urls import path
from content import views

urlpatterns = [
    path('upload/', views.UploadFeed,name='upload'),
    path('feed/delete/<int:id>', views.delete_feed, name='delete-feed'),
]
