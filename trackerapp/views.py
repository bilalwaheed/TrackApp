# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.urls import reverse
from django.views import generic

from trackerapp.forms import RegisterForm, SignInForm, TicketCreationForm, FeatureCreationForm
from trackerapp.models import TicketTracking


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        all_tickets = TicketTracking.objects.all()
        return render(request, self.template_name, {'all_tickets':all_tickets})

class LoginView(generic.TemplateView):
    template_name = 'login.html'

    def post(self, request, **Kwargs):
        if request.method == 'Post':
            form = SignInForm(request.POST)
            if form.is_valid():
                messages.success(request, 'login in Successfully!', extra_tags='alert')
                return redirect('index')
            else:
                messages.warning(request, 'Login field', extra_tags='alert')
        else:
            form = SignInForm()
        return render(request, self.template_name, {'form': form})


class RegistrationView(generic.TemplateView):
    template_name = 'register.html'

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Registered successfully! Please login', extra_tags='alert')
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('login')
            else:
                messages.warning(request, 'Registration failed', extra_tags='alert')
        else:
            form = RegisterForm()
        return render(request, self.template_name, {'form': form})


class TicketCreationView(generic.TemplateView):
    template_name = 'ticket_creation.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            import pdb;pdb.set_trace()
            form = TicketCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = TicketCreationForm()
        return render(request, self.template_name, {'form': form})

class FeatureCreationView(generic.TemplateView):
    template_name = 'feature_request.html'

    def post(self, request, **kwargs):
        if request.method == 'POST':
            # import pdb;pdb.set_trace()
            form = FeatureCreationForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('index')
        else:
            form = FeatureCreationForm()
        return render(request, self.template_name, {'form': form})

class TicketEditView(generic.TemplateView):
    template_name = 'ticket_creation.html'

    def post(self,request, **kwargs):
        ticket_id = kwargs.get('ticket_id')
        ticket = TicketTracking.objects.filter(id=ticket_id).first()
        ticket.ticket_name = self.request.POST.get('ticket_name')
        ticket.ticket_comment = self.request.POST.get('ticket_comment')
        ticket.ticket_status = self.request.POST.get('ticket_status')
        ticket.save()
        return redirect(reverse('dashboard'))



