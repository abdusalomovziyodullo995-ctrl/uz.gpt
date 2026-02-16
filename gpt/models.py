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







# class kirish(models.Model):
#     full_name = models.CharField(max_length=51)
#     age = models.PositiveIntegerField()
#     phone = models.CharField()
#     email = models.EmailField()
#     password = models.TextField()



# class ai(models.Model):
#     name = models.CharField(max_length=51)
#     kasbi = models.CharField()
#     harakter = models.TextField()
#     rasm = models.ImageField()



# class chat_history(models.Model):
#     user_id = models.ForeignKey()
#     ai_id = models.ForeignKey()
#     text = models.TextField()



    





