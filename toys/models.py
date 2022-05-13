from django.db import models

"""
   A class used to represent an Toy model class
   
"""


class Toy(models.Model):
    toy_item = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.toy_item) + ": $" + str(self.price)
