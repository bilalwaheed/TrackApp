from __future__ import unicode_literals
from django.db import models

class TicketTracking(models.Model):
    ticket_name = models.CharField(max_length=250)
    ticket_comment = models.CharField(max_length=250)
    ticket_status = models.CharField(max_length=250)

class Bug(models.Model):
    bug_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    solution = models.CharField(max_length=250)

class Feature(models.Model):
    feature_name = models.CharField(max_length=250)











