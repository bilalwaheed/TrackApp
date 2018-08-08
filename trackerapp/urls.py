from django.conf.urls import url
from trackerapp import views
from trackerapp.views import IndexView, DashboardView, LoginView, RegistrationView, TicketCreationView, \
    FeatureCreationView, TicketEditView
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
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^add/ticket/$', TicketCreationView.as_view(), name='add_ticket'),
    url(r'^add/feature/$', FeatureCreationView.as_view(), name='add_feature'),
    url(r'^edit/ticket/(?P<ticket_id>\d+)$', TicketEditView.as_view(), name='edit_ticket')


]
