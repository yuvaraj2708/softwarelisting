from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields if needed
    is_staff = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SoftwareList(models.Model):
    image = models.ImageField(upload_to='software_images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()
    software_description = models.TextField()
    software_features = models.TextField()
    software_specialties = models.TextField()
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
