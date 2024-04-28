from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    fullName = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={"placeholder":"FisrtName LastName"}))
    email = forms.EmailField(required=True,max_length=100, widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    messageTopic = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={"placeholder":"Enter Subject"}))
    messageBody = forms.CharField(required=True,max_length=1000, widget=forms.Textarea(attrs={"placeholder":"Message Body Here...","cols":"15","row":"8"}))
    
    class Meta:
        model = Feedback
        exclude = ('createdAt_UTC',)
