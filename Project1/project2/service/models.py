from django.db import models
class Solo(models.Model):
    mai1=models.CharField(max_length=50)
    mai2=models.CharField(max_length=100)
    mai3=models.CharField(max_length=100,default='net')
# Create your models here.
