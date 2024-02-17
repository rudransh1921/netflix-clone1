from django.db import models
class Solo1(models.Model):
    email=models.EmailField(max_length=100)
    password=models.TextField(max_length=100)

# Create your models here.
