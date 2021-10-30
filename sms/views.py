# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail

from .models import Message

def homepage(request):
    context = {'data': 'For future use'}
    return render(request, 'index.html', context)

@csrf_exempt
def receive(request):
    email_to = settings.EMAIL_TO
    email_from = settings.EMAIL_FROM
    phone_from = request.POST.get('From')
    subject = "SMS from %s" % (phone_from,)
    phone_to = request.POST.get('To')
    body = request.POST.get('Body')
    message = "From: %s To: %s Message: %s" % (phone_from, phone_to, body)

    if not body:
        raise Http404("No message was sent.")

    new_message = Message(message_to=phone_to, message_from=phone_from, message_body=body)
    new_message.save()
    send_mail(subject, message, email_from, [email_to], fail_silently=False,)

    return HttpResponse('')
