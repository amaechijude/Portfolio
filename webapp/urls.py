from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mail_view', views.mail_view, name='mail_view'),
]
