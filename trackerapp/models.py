from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class TicketTracking(models.Model):
    TO_DO = '1'
    IN_PROGRESS = 2
    REVIEW = 3
    DONE = 4

    STATUS = ((TO_DO, 'TO Do'),
              (IN_PROGRESS, 'In Progress'),
              (DONE, 'Done'),
              (REVIEW, 'Review'),
              )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_name = models.CharField(max_length=250)
    ticket_comment = models.CharField(max_length=250)
    ticket_status = models.SmallIntegerField(choices=STATUS)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Ticket Tracking'


class Bug(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bug_name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    solution = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)


class Feature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)
