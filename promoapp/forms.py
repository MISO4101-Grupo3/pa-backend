from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class PromoUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
        exclude = ['username']


class PromoUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
        exclude = ['username']
