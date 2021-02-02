from typing import ClassVar
from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField, TextField
from django.urls import reverse
from django.utils.text import slugify   


# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

class Category(models.Model):
    """Categories of sites"""
    name = models.CharField(max_length=80)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name


class News(models.Model):
    """News model"""
    name = CharField(max_length=80)
    topic = TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name[:10] + ".."

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Contact(models.Model):
    """Customer name"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    text = models.TextField()

    def __str__(self):
        return 'Message from : ' + self.first_name + ' ' + self.last_name + ' | Phone : ' + str(self.phone) + ' | Message : ' + self.text


class Subscribe(models.Model):
    """Subscribe """
    email = EmailField()

    def __str__(self):
        return self.email


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    subtitle = TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField()
    image = models.ImageField(null=True, blank=True)

    #def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)
        #super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.subtitle[0:250]

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class BlogComment(models.Model):

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return f'Comment by {self.name}'