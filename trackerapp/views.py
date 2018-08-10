# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.urls import reverse
from django.views import generic

from trackerapp.forms import RegisterForm, SignInForm, TicketCreationForm, FeatureCreationForm, BugCreationForm
from trackerapp.models import TicketTracking, Feature, Bug


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        all_tickets = TicketTracking.objects.all()
        all_features = Feature.objects.all()
        all_bugs = Bug.objects.all()
        return render(request, self.template_name,
                      {'all_tickets': all_tickets, 'all_features': all_features, 'all_bugs': all_bugs})


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


class TicketCreationView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'ticket_creation.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = TicketCreationForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            post_data = request.POST.copy()
            post_data['user'] = request.user.id
            form = TicketCreationForm(post_data)
            if form.is_valid():
                messages.success(request, 'Ticket Created successfully!', extra_tags='alert')
                form.save()
                return redirect('ticket')
        else:
            form = TicketCreationForm()
        return render(request, self.template_name, {'form': form})


class BugCreationView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'Bug_request.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = BugCreationForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            post_data = request.POST.copy()
            post_data['user'] = request.user.id
            form = BugCreationForm(post_data)
            if form.is_valid():
                messages.success(request, 'Bug created successfully!', extra_tags='alert')
                form.save()
                return redirect('bug')
        else:
            form = BugCreationForm()
        return render(request, self.template_name, {'form': form})


class FeatureCreationView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'feature_request.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = FeatureCreationForm()
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        if request.method == 'POST':
            post_data = request.POST.copy()
            post_data['user'] = request.user.id
            form = FeatureCreationForm(post_data)
            if form.is_valid():
                messages.success(request, 'Feature Created successfully!', extra_tags='alert')
                form.save()

                return redirect('feature')
        else:
            form = FeatureCreationForm()
        return render(request, self.template_name, {'form': form})


class TicketEditView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'ticket_creation.html'

    def post(self, request, **kwargs):
        ticket_id = kwargs.get('ticket_id')
        ticket = TicketTracking.objects.filter(id=ticket_id).first()
        ticket.ticket_name = self.request.POST.get('ticket_name')
        ticket.ticket_comment = self.request.POST.get('ticket_comment')
        ticket.ticket_status = self.request.POST.get('ticket_status')
        ticket.save()
        messages.success(request, 'Ticket Edit successfully!', extra_tags='alert')

        return redirect(reverse('ticket'))


class FeatureEditView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'feature_request.html'

    def post(self, request, **kwargs):
        feature_id = kwargs.get('feature_id')
        feature = Feature.objects.filter(id=feature_id).first()
        feature.feature_name = self.request.POST.get('feature_name')
        feature.save()
        messages.success(request, 'Feature Edit successfully!', extra_tags='alert')
        return redirect(reverse('feature'))


class BugEditView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'Bug_request.html'

    def post(self, request, **kwargs):
        bug_id = kwargs.get('bug_id')
        bug = Bug.objects.filter(id=bug_id).first()
        bug.bug_name = self.request.POST.get('bug_name')
        bug.description = self.request.POST.get('description')
        bug.solution = self.request.POST.get('solution')
        bug.save()
        messages.success(request, 'Bug Edit successfully!', extra_tags='alert')
        return redirect(reverse('bug'))


class TicketView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'ticket.html'

    def get(self, request, *args, **kwargs):
        all_tickets = TicketTracking.objects.filter(user=self.request.user)
        return render(request, self.template_name, {'all_tickets': all_tickets})

        # return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class FeatureView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'feature.html'

    def get(self, request, *args, **kwargs):
        all_features = Feature.objects.all()
        return render(request, self.template_name, {'all_features': all_features})


class BugView(generic.TemplateView):
    template_name = 'bugs.html'

    def get(self, request, *args, **kwargs):
        all_bugs = Bug.objects.all()
        return render(request, self.template_name, {'all_bugs': all_bugs})
