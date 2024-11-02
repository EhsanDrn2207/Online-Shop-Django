from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse('login')
