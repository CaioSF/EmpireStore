from django.db import models

class Product(models.Model):
    title = models.CharField('Títutlo', max_length=120)
    description = models.TextField('Description', max_length=None, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title