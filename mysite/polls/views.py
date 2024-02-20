from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os

def index(request):
    return render(request, 'polls/index.html')