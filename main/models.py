from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # country = models.CharField(max_length=30)