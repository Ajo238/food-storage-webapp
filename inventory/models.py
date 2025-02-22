from django.db import models
from django.utils.timezone import now

"""
This model will store food items, their quantity, unit of measurement, expiry date, and when they were added.

"""


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Dairy', 'Dairy'),
        ('Meat', 'Meat'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Grains', 'Grains'),
        ('Other', 'Other'),
    ])
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, help_text="e.g., kg, g, liters, pieces")
    expiry_date = models.DateField()
    added_on = models.DateTimeField(default=now)

    def is_expired(self):
        return self.expiry_date < now().date()

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"
