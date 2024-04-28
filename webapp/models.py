from django.db import models
from django.core.validators import URLValidator

from django_resized import ResizedImageField # Compreess image
#from ckeditor.fields import RichTextField
# Create your models here.
class Feedback(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    messageTopic = models.CharField(max_length=100)
    messageBody = models.TextField(max_length=1000)
    createdAt_UTC = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(f"{self.fullName}")

class Portfolio(models.Model):
    title = models.CharField(blank=True,max_length=200)
    sub_title = models.CharField(blank=True,max_length=200)
    image = ResizedImageField(blank=True,quality=70,upload_to='portfolio')
    created_at = models.DateTimeField(auto_now=True)
    github_url = models.URLField(validators=[URLValidator()], max_length=300, blank=True)
    link_url = models.URLField(validators=[URLValidator()], max_length=300, blank=True)

    def __str__(self):
        return(f"{self.title}")

class Blog(models.Model):
    title = models.CharField(blank=False,max_length=200)
    image = ResizedImageField(blank=True,quality=70,upload_to='portfolio')
    #body = RichTextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(f"{self.title}")

class Timeline(models.Model):
    duration = models.CharField(blank=False,max_length=20)
    job_title = models.CharField(blank=False,max_length=50)
    company = models.CharField(blank=False,max_length=50)
    job_desc = models.CharField(blank=False,max_length=200)

    def __str__(self):
        return(f"{self.job_title} : {self.company}")
