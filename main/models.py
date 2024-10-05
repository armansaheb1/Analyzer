from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    mobile = models.CharField(_("Phone Number"), max_length=10, unique=True)

    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.mobile


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)


class Service(models.Model):
    slug = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100)
    prompt = models.TextField(null=True)
    description = models.CharField(max_length=1000)
    variables = models.JSONField()
    price = models.IntegerField()
    icon = models.CharField(null=True, max_length=20)
    color = models.CharField(null=True, max_length=6)
    category = models.ForeignKey(
        Category, related_name="services", on_delete=models.CASCADE
    )


class NewsSite(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()


class NewsIntrest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)


class NewsReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=90)
    text = models.CharField(max_length=1000)
    pic = models.CharField(max_length=1000)
    subject = models.CharField(max_length=100)
