from django import forms

class JobApplyForm(forms.Form):
    resume = forms.FileField()