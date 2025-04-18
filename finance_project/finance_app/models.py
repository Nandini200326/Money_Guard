from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TYPE = (
    ('Positive','Positive'),
    ('Negative','Negative'),
)
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField(default=0.0)
    balance= models.FloatField(null=True,blank=True)
    expenses = models.FloatField(default=0.0)
    
    