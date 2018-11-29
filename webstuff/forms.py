from django import forms

class HeartForm(forms.Form):
    attrs = {
        'class': 'w3-input w3-border',
        'type': 'text'
    }
    attrs.update({'placeholder' : 'Name'})
    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Age'})
    age = forms.CharField(label='Your age', widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '1/0'})
    gender = forms.CharField(label = 'Gender' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '1/0'})
    chestpain = forms.CharField(label = 'Chest pain?' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Blood Pressure (mm Hg)'})
    bloodpressure = forms.CharField(label='Blood pressure', widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Chol (mg/dl)'})
    chol = forms.CharField(label = 'Cholestoral number' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '1/0'})
    fbs = forms.CharField(label = 'Fasting blood sugar > 120 mg/dl' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '0/1/2'})
    restecg = forms.CharField(label = 'Resting electrocardiographic results' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Maximum heart rate achieved'})
    thalach = forms.CharField(label = 'Thalach' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '1/0'})
    exang = forms.CharField(label = 'Exercise induced angina' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'ST depression'})
    oldpeak = forms.CharField(label = 'Oldpeak' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '1/2/3'})
    slope = forms.CharField(label = 'Slope' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '0/1/2/3'})
    ca = forms.CharField(label='Ca', widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : '3/6/7'})
    thal = forms.CharField(label='Thal', widget=forms.TextInput(attrs=attrs))

    
    
    
    
    
    
    
    
    
    # attribute6 = forms.ChoiceField(label = 'Sex', choices=("Male", "Female"), widget=forms.SelectMultiple(attrs=attrs))
