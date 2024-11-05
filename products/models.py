from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()


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

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.id])


class Comment(models.Model):
    STARTS_CHOICES = (
        ('5', 'Perfect'),
        ('4', 'good'),
        ('3', 'normal'),
        ('2', 'bad'),
        ('1', 'very bad'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    stars = models.CharField(choices=STARTS_CHOICES, max_length=10)
    is_active = models.BooleanField(default=True)
    is_recommend = models.BooleanField(default=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.product.id])
