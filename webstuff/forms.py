from django import forms

class HeartForm(forms.Form):
    attrs = {
        'class': 'w3-input w3-border',
        'type': 'text'
    }

    attribute1 = forms.CharField(label='Your name', widget=forms.TextInput(attrs=attrs))
    attribute2 = forms.CharField(label='Your age', widget=forms.TextInput(attrs=attrs))
    attribute3 = forms.CharField(label='Blood pressure', widget=forms.TextInput(attrs=attrs))
    attribute4 = forms.CharField(label='Do you smoke?', widget=forms.TextInput(attrs=attrs))
    attribute5 = forms.CharField(label='Do you do sports often?', widget=forms.TextInput(attrs=attrs))
    attribute6 = forms.CharField(label = 'Sex' , widget=forms.TextInput(attrs=attrs))
