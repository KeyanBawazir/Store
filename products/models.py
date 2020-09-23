from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length= 2000, null= True, blank= True)
    def get_absolute_url(self):
        return reverse('product_details', args=(self.pk,))
    def __str__(self):
        return self.title