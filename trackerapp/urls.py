from django.conf.urls import url
from trackerapp import views
from trackerapp.views import IndexView, DashboardView, LoginView, RegistrationView, TicketCreationView, \
    FeatureCreationView, TicketEditView, FeatureEditView, BugCreationView, BugEditView, TicketView, FeatureView, BugView
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
    url(r'^add/bug/$', BugCreationView.as_view(), name='add_bug'),
    url(r'^edit/ticket/(?P<ticket_id>\d+)$', TicketEditView.as_view(), name='edit_ticket'),
    url(r'^edit/feature/(?P<feature_id>\d+)$', FeatureEditView.as_view(), name='edit_feature'),
    url(r'^edit/bug/(?P<bug_id>\d+)$', BugEditView.as_view(), name='edit_bug'),
    url(r'^ticket/$', TicketView.as_view(), name='ticket'),
    url(r'^feature/$', FeatureView.as_view(), name='feature'),
    url(r'^bug/$', BugView.as_view(), name='bug')

]
