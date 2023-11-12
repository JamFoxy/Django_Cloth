from django.db import models

class CustomerCL(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductCL)
    order_date = models.DateField(auto_now_add=True)
