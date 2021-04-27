from django.db import models

# Create your models here.
import os
from django.db import models
from django.conf import settings


"""
class User(models.Model):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
	# user entered
    name = models.CharField("name", max_length=30, null=True)
    passcode = models.CharField("passcode", max_length=6, null=True)
	# grab from twilio any time someone connects
    number = models.CharField("phone number", max_length=15)
"""

# class IVRUser(models.Model):
#     class Meta:
#         verbose_name = 'IVR User'
#         verbose_name_plural = 'IVR Users'

#     # Generate path from user ID
#     @staticmethod
#     def user_directory_path(instance, filename):
#         # file will be uploaded to MEDIA_ROOT/users/user_<id>/filename
#         return f"users/user{instance."



#     # Grabbed from Twilio, must be unique, used to find user object
#     number = models.CharField("phone number", max_length=15, primary_key=True)

#     # Recordings provided by user
#     name_audio = models.FileField()



class Title(models.Model):
    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
    GENRES = [
        ('SC', 'Science'),
        ('HI', 'History'),
        ('LI', 'Literature'),
        ('MA', 'Math'),
        ('BI', 'Biography'),
        ('RE', 'Reference'),
    ]
	# user entered
    name = models.CharField("book title", max_length=50, null=True)
    author = models.CharField("book author", max_length=50, null=True)
    # reader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    genre = models.CharField("genre", max_length=2, choices=GENRES, null=True)
	# auto generated
    files = models.CharField("file path", max_length=200)