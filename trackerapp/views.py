# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from trackerapp.forms import RegisterForm


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'


class LoginView(generic.TemplateView):
    template_name = 'login.html'


class RegistrationView(generic.TemplateView):
    template_name = 'register.html'

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, self.template_name, {'form': form})
