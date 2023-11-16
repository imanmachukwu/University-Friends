from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    word = models.CharField(max_length=100)
    love_most = models.TextField()
    department = models.TextField()
    image = models.ImageField(upload_to='images/')
