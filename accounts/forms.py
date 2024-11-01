from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email')


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email')
