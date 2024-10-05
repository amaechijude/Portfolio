import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# from .models import Feedback, Portfolio, Blog, Timeline
from.forms import FeedbackForm

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def feedback_mail(name, email, topic, message):
    body = f"Message from: {name}\nEmail: {email}\n\n{message}"
    reciever_email = settings.EMAIL_HOST_USER
    send_mail(
        topic,
        body,
        email,
        [reciever_email],
        fail_silently=False
        )


def get():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return None
    data = response.json()
    return data['ip']

def index(request):
    """Home Page"""
    form = FeedbackForm()
    context = {"form":form,"ip":get()}
    return render(request, 'index.html',context)


def mail_view(request):
    """Mail Sending"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fullName = form.cleaned_data['fullName']
            email = form.cleaned_data['email']
            messageTopic = form.cleaned_data['messageTopic']
            messageBody = form.cleaned_data['messageBody']
            #send mail
            try:
                feedback_mail(fullName, email, messageTopic, messageBody)
                return JsonResponse({"message":"Feedback Submitted"})
            except TimeoutError as e:
                return JsonResponse({"message":f"{e}"})

        return JsonResponse({"message":f"{form.errors}"})
    return JsonResponse({"message":"Invalid Method"})


def blogs(request):
    return render(request, 'blog.html')
