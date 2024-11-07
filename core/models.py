from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    stock_quantity=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.name