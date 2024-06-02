from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField()
    preparation_method = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

