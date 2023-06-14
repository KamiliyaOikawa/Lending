from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)



class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos', blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telegram = models.URLField(blank=True)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.user.username