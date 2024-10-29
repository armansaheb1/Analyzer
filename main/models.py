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

class StaticEntry(models.Model):
    name = models.CharField(max_length=90, null=True)
    options = models.JSONField()
    prompt = models.TextField(null=True)

class IdeaStaticEntry(models.Model):
    name = models.CharField(max_length=90, null=True)
    options = models.JSONField()
    prompt = models.TextField(null=True)


class Service(models.Model):
    slug = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100)
    prompt = models.TextField(null=True)
    description = models.CharField(max_length=1000)
    variables = models.JSONField()
    static_variables = models.ManyToManyField(StaticEntry)
    price = models.IntegerField()
    icon = models.CharField(null=True, max_length=50)
    icon_image =models.ImageField(upload_to='icons', null=True)
    button_name=models.CharField(max_length=100, null=True)
    highlight=models.CharField(max_length=100, null=True)
    color = models.CharField(null=True, max_length=6)
    category = models.ForeignKey(
        Category, related_name="services", on_delete=models.CASCADE
    )


class NewsService(models.Model):
    name = models.CharField(max_length=100)
    prompt = models.TextField(null=True)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()


class NewsSite(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()


class NewsIntrest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

class SocialIntrest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    twitter = models.BooleanField(null=True)
    telegram = models.BooleanField(null=True)
    channels = models.JSONField()


class NewsReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=90, null=True)
    text = models.CharField(max_length=1000, null=True)
    pic = models.CharField(max_length=1000, null=True)
    subject = models.CharField(max_length=100, null=True)
    resource = models.CharField(max_length=100, null=True)


class Tone(models.Model):
    name = models.CharField(max_length=90, null=True)


class Format(models.Model):
    name = models.CharField(max_length=90, null=True)


