from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from cloudinary.models import CloudinaryField




class Category(models.Model):
    name = models.TextField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Product(AbstractBaseUser):
    # vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.TextField(max_length=3)
    categories = models.ManyToManyField(Category)
    image = models.FileField(upload_to='Commerce-images')

    REQUIRED_FIELDS = ["vendor"]

    def __str__(self):
        return self.name


# {
# "name": "First product",
# "price": "200",
# "size": "XL",
# "categories": ["Clothes"],
# "image": 
# }