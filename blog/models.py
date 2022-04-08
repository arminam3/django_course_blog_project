from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import  reverse

class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'published'),
        ('drf', 'draft'),
    )

    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey('auth.User', related_name='user_author' , on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES , max_length=100)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

    def __str__(self):
        return self.title
