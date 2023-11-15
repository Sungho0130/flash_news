from django.db import models

# Create your models here.
class Crawring(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.CharField(max_length=100)
    src = models.CharField(max_length=100,default='default_value')
    summarize = models.CharField(max_length=100, default='default_value')

