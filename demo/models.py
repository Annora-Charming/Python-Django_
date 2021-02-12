from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=40, blank=False, unique=True)
    description=models.TextField(max_length=500, blank=True)
    price=models.DecimalField(default=0, max_digits=6, decimal_places=2)
    published=models.DateTimeField
    is_published=models.BooleanField
    cover=models.ImageField(upload_to='covers/')
