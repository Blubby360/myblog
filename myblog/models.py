from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField('email address')
    date_joined = models.DateTimeField('date joined', auto_now_add = True)
    about = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_title = models.CharField(max_length = 200)
    post_content = models.TextField()
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.post_title