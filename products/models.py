from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    # cover = models.ImageField(upload_to="covers/")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("product-detail", args=[self.id])
