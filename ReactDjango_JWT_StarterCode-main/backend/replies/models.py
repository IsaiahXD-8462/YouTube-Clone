from django.db import models
from authentication.models import User

# Create your models here.
class Reply(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(User, on_delete=models.CASCADE)