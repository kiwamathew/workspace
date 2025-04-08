from django.db import models
import datetime

# Create your models here.
class Savings(models.Model):
    name = models.TextField(blank=False)
    occupation = models.TextField()
    amount = models.IntegerField(blank=False)
    date = models.DateField()
    transaction_id = models.TextField(unique=True, blank=False)
    
# Tuesday 8th April 2025 class
class User(models.Model):
    name = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=255)
    # Role can be text, or charfield.
    # Administrator, Operations, cashier
    role = models.TextField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

class Supplier(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField() # Charfield(max_length=14)
    address = models.TextField()

class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.TextField()
    image = models.ImageField()
    sku = models.TextField(unique=True)
    price = models.IntegerField()
    selling_price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    expiry_date = models.DateField()
    supplier_id = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null = True)

class Inventory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    details = models.TextField()
    current_date = models.DateField(auto_now_add=True)

class Transaction(models.Model):
    tx_id = models.TextField(unique=True)
    product-id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # kind = models.CharField(max_length=10) # Buy or Sell
    total_amount = models.IntegerField()
    method = models.CharField(max_length=15) # Cash, Bank, Card, mobile Money, Loyalty
    customer_name = models.TextField9
    customer_phone = models.TextField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    