from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name