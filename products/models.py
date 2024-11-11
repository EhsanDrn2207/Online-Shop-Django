from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
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


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(is_active=True)


class Comment(models.Model):
    STARTS_CHOICES = (
        ('5', _('Perfect')),
        ('4', _('good')),
        ('3', _('normal')),
        ('2', _('bad')),
        ('1', _('very bad')),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name=_('comment-author'))
    body = models.TextField(verbose_name=_('comment-text'))
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    stars = models.CharField(choices=STARTS_CHOICES, max_length=10, verbose_name=_('score'))
    is_active = models.BooleanField(default=True)
    is_recommend = models.BooleanField(default=True, verbose_name=_('recommend'))

    # Manager
    object = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.product.id])
