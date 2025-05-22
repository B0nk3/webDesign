from django.db import models
# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
class Post(models.Model):
    title = models.CharField(max_length = 100)
    post_date = models.DateField()
    image = models.ImageField(upload_to = 'static/')
    paragraph = models.TextField(max_length=100)
    