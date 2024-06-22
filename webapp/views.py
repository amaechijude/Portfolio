from django.shortcuts import render, redirect
from django.contrib import messages

# from .models import Feedback, Portfolio, Blog, Timeline
from.forms import FeedbackForm

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def feedback_mail(name, email, topic, message,):
    body = f"Message from: {name}\nEmail: {email}\n\n{message}"
    reciever_email = settings.EMAIL_HOST_USER
    send_mail(
            topic,
            body,
            email,
            [reciever_email],
            fail_silently=False
        )



def index(request):
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
                messages.info(request, "Feedback Submitted")
                return redirect('index')
            except TimeoutError:
                messages.info(request, "O di egwu")
                return redirect('index.html')
   
    form = FeedbackForm()
    context = {"form":form}
    return render(request, 'index.html',context)
