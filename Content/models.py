from email.mime import image
from django.db import models
from accounts.models import UserModel


# Create your models here.
class FeedModel(models.Model):
    class Meta:
        db_table = "feed"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.TextField()
    like_count = models.IntegerField()