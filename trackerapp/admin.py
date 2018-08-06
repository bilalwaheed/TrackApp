from __future__ import unicode_literals

from django.contrib import admin

from trackerapp.models import TicketTracking,Bug,Feature


class TicketTrackingAdmin(admin.ModelAdmin):
    model = TicketTracking
    list_display = ('ticket_name', 'ticket_comment', 'ticket_status')

class BugAdmin(admin.ModelAdmin):
    model = Bug
    list_display = ('bug_name', 'description', 'solution')

class FeatureAdmin(admin.ModelAdmin):
    model = Feature
    list_display = ('feature_name')






admin.site.register(TicketTracking,TicketTrackingAdmin)
admin.site.register(Bug,BugAdmin)
admin.site.register(Feature)






