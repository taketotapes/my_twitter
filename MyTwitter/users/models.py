from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'User info: {self.username}-{self.date_joined}'


class UserProfile(models.Model):
    userprofile = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # def get_followers(self):
    #     return self.followers.all()
    #
    # def get_following(self):
    #     return self.user.following.all()
