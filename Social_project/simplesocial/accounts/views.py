from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from django.views import View
from django.contrib.auth import logout
from django.views.generic import CreateView
# Create your views here.
class Signup(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class CustomLogoutView(View):
    def get(self,request):
        logout(request)
        return  redirect('thanks')