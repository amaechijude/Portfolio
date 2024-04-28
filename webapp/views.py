from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Feedback, Portfolio, Blog, Timeline
from.forms import FeedbackForm

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Feedback Submitted")
            return redirect('index')
        messages.info(request, "O di egwu")
        return redirect('index.html')
    blogs = Blog.objects.all()
    works = Portfolio.objects.all()
    timeline = Timeline.objects.all()
    form = FeedbackForm()
    context = {"blogs": blogs, "works":works,"timeline":timeline, "form":form}
    return render(request, 'index.html',context)
