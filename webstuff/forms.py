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

    attrs.update({'placeholder' : 'Male/Female'})
    sex = forms.CharField(label = 'Gender' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Yes/No'})
    chestpain = forms.CharField(label = 'Chest pain?' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Blood Pressure (mm Hg)'})
    bloodpressure = forms.CharField(label='Blood pressure', widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Chol (mg/dl)'})
    chol = forms.CharField(label = 'Cholestoral number' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Yes/No'})
    fbs = forms.CharField(label = 'Fasting blood sugar > 120 mg/dl' , widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Smoke'})
    attribute4 = forms.CharField(label='Do you smoke?', widget=forms.TextInput(attrs=attrs))

    attrs.update({'placeholder' : 'Sport'})
    attribute5 = forms.CharField(label='Do you do sports often?', widget=forms.TextInput(attrs=attrs))
    
    
    
    
    attrs.update({'placeholder' : '0: normal 1: having ST-T wave abnormality 2: showing probable or definite left ventricular hypertrophy by Estes criteria'})
    restecg = forms.CharField(label = 'Resting electrocardiographic results' , widget=forms.TextInput(attrs=attrs))
    attrs.update({'placeholder' : 'Make Love'})
    attribute6 = forms.CharField(label = 'Sex' , widget=forms.TextInput(attrs=attrs))
    attrs.update({'placeholder' : 'Make Love'})
    attribute6 = forms.CharField(label = 'Sex' , widget=forms.TextInput(attrs=attrs))
    attrs.update({'placeholder' : 'Make Love'})
    attribute6 = forms.CharField(label = 'Sex' , widget=forms.TextInput(attrs=attrs))
    attrs.update({'placeholder' : 'Make Love'})
    attribute6 = forms.CharField(label = 'Sex' , widget=forms.TextInput(attrs=attrs))
    # attribute6 = forms.ChoiceField(label = 'Sex', choices=("Male", "Female"), widget=forms.SelectMultiple(attrs=attrs))
