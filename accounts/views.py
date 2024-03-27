from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

from .forms import CustomUserCreationForm

class SignupViewPage(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'