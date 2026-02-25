from django.db import models

from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _



class User_profile(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Ai_agent(models.Model):
    name = models.CharField(max_length=51)
    kasbi = models.CharField(max_length=51)
    shaxsiyat = models.TextField()
    icon = models.CharField()

    def __str__(self):
        return f"{self.name} - {self.kasbi}"


class History(models.Model):
    FROM = [
        ("user" , "User"),
        ("agent", "Agent"),
    ]

    user_id = models.ForeignKey(User_profile , on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Ai_agent , on_delete=models.CASCADE)
    text = models.TextField()
    kimdan = models.CharField(choices=FROM)










