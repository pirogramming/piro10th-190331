from django.contrib.auth.models import AbstractUser
from django.db import models


class User (AbstractUser):
    pass


class Document (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #@TODO 유저 이름 맞추기
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment (models.Model):
    text = models.CharField(max_length=300)
    doc = models.ForeignKey(Document, on_delete=models.CASCADE)
    #@TODO 유저 이름 맞추기
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
