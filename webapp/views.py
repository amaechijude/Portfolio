from django.http import JsonResponse
from django.shortcuts import render

# from .models import Feedback, Portfolio, Blog, Timeline
from.forms import FeedbackForm

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    """Home Page"""
    form = FeedbackForm()
    context = {"form":form,"ip":"ip"}
    return render(request, 'index.html',context)


##### Email sending function ######
async def feedback_mail(name, email, topic, message):
    """SendMail function"""
    body = f"""
        Message from: {name}
        Email: {email}

        {message}
        """
    reciever_email = settings.EMAIL_HOST_USER
    try:
        send_mail(topic, body, email, [reciever_email],fail_silently=False)
    except:
        return False
    return True


########## Email Send View ##########
async def mail_view(request):
    """Mail Sending"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fullName = form.cleaned_data['fullName']
            email = form.cleaned_data['email']
            messageTopic = form.cleaned_data['messageTopic']
            messageBody = form.cleaned_data['messageBody']
            #send mail
            ms = await feedback_mail(fullName, email, messageTopic, messageBody)
            if ms == True:
                # print("Feedback Submitted")
                return JsonResponse({"message":"Feedback Submitted"})
            # print("Connection error")
            return JsonResponse({"message": "Connection error"})
        # print(f"{form.errors}")
        return JsonResponse({"message":f"{form.errors}"})
    # print("Invalid Method")
    return JsonResponse({"message":"Invalid Method"})
