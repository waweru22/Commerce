from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from cloudinary.models import CloudinaryField




class Category(models.Model):
    name = models.TextField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.FileField(upload_to='Commerce-images')


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.TextField(max_length=3)
    categories = models.ManyToManyField(Category)
    feature_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    images = models.JSONField()

    REQUIRED_FIELDS = ["name", "price", "size"]

    def __str__(self):
        return self.name
    

# {
# "name": "First product",
# "price": "200",
# "size": "XL",
# "categories": ["Clothes"],
# "image": 
# }