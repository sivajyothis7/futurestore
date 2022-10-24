from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):

    category_options=(
        ("mobiles","mobiles"),
        ("earphones","earphones"),
        ("watches","watches"),
    )

    category_name=models.CharField(choices=category_options,max_length=50,unique=True)
    category_image=models.ImageField(upload_to="cat_images",null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images",null=True)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.product_name

class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")

    )
    status=models.CharField(max_length=120,choices=options,default="in-cart")
    qty=models.PositiveIntegerField()


class Orders(models.Model):
    product= models.ForeignKey(Products, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    options= (
        ("order-placed", "order-placed"),
        ("dispatched", "dispatched"),
        ("in-transit", "in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled")

    )
    status = models.CharField(max_length=120, choices=options, default="order-placed")
    delivery_address=models.CharField(max_length=250,null=True)
    expected_delivery_date=models.DateTimeField(null=True)


class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comments=models.CharField(max_length=120)
    rating=models.PositiveIntegerField()

class Wishlist(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Enquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=120)

