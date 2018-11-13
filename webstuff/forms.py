from django import forms

class HeartForm(forms.Form):
    attribute1 = forms.CharField(label='Your name')
    attribute2 = forms.CharField(label='Your age')
    attribute3 = forms.CharField(label='Blood pressure')
    attribute4 = forms.CharField(label='Do you smoke?')
    attribute5 = forms.CharField(label='Do you do sports often?')