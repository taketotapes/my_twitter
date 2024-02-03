from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class FollowForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
    user_to_follow = forms.IntegerField()


