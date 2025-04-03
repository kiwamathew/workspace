from django.db import models
import datetime

# Create your models here.
class Savings(models.Model):
    name = models.TextField(blank=False)
    occupation = models.TextField()
    amount = models.IntegerField(blank=False)
    date = models.DateField()
    transaction_id = models.TextField(unique=True, blank=False)
    
