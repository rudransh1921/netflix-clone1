from django.db import models
from tinymce.models import HTMLField
class new(models.Model):
    first=models.EmailField(max_length=100)
    second=models.CharField(max_length=100)
# Create your models here.
