from django.conf.urls import url
from trackerapp import views
from trackerapp.views import IndexView, DashboardView, LoginView, RegistrationView
from django.contrib import admin

from django.contrib.auth.views import login, logout

from Tracker import settings
from trackerapp.forms import SignInForm

urlpatterns = [
    url(r'^accounts/login/$', login, {
        'template_name': 'login.html',
        'authentication_form': SignInForm,
    }, name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    # url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration')

]
