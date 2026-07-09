from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class cartitem(models.Model):
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def total_price(self):
        return self.product.price*self.quantity
