from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()


    def __str__(self):
        return self.name

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='client_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Hero(models.Model):
    image = models.ImageField(upload_to='hero_images/', null=True, blank=True)
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.heading