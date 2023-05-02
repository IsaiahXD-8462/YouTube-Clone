from django.db import models
from authentication.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Comment(models.Model):
    video_id = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)