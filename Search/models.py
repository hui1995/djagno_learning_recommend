from django.db import models

# Create your models here.

class Result(models.Model):
    title=models.CharField(max_length=2048)
    keyword=models.CharField(max_length=256)
    content=models.TextField()
    create_time=models.DateTimeField()
    create_user=models.CharField(max_length=1024)
    url=models.CharField(max_length=2048)

