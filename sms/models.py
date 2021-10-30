# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import date


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message_from = models.CharField(max_length=200)
    message_to = models.CharField(max_length=200)
    message_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '%s %s %s' % (date(self.created_at,'d M Y'), self.message_from, self.message_body)
