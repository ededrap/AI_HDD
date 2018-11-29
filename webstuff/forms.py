from django import forms

class HeartForm(forms.Form):
    attrs = {
        'class': 'w3-input w3-border',
        'type': 'text'
    }
    attrs.update({'placeholder' : 'Name'})
    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs=attrs))

    age = forms.ChoiceField(label='Your age (dalam tahun)', choices=((0,"< 20 tahun"), 
        (1,"20 < x < 30"), (2,"30 < x < 40"), (3,"40 < x < 50"), (4,"50 < x < 60"), 
        (5,"60 < x < 70"), (6, "70 ke atas")), widget=forms.Select(attrs=attrs))
    sex = forms.ChoiceField(label = 'Sex', choices=((0,"Female"), (1,"Male")), widget=forms.Select(attrs=attrs))
    cp = forms.ChoiceField(label='Chest pain', choices=((-9, "Unknown"), (1,"Typical Angina"), (2,"Atypical Angina"), 
        (3, "Non-anginal Pain"), (4, "Asymptomatic")), widget=forms.Select(attrs=attrs))
    trestbps = forms.ChoiceField(label='Resting Blood Pressure (mmHg)', choices=((-9, "Unknown"), (0,"< 120"), 
        (1,"120 < x < 130"), (2, "130 < x < 140"), (3, "140 < x < 180"), (4, "180 ke atas")), 
        widget=forms.Select(attrs=attrs))
    chol = forms.ChoiceField(label='Cholestoral level (mg/dl)', choices=((-9, "Unknown"), (0,"< 200"), 
        (1,"200 < x < 230"), (2, "230 < x < 260"), (3, "260 < x < 290"), (4, "290 < x < 320"), 
        (5, "320 ke atas")), widget=forms.Select(attrs=attrs))
    fbs = forms.ChoiceField(label='Fasting Blood Sugar > 120mg/dl?', choices=((-9, "Unknown"), (1,"Yes"), (0,"No")), widget=forms.Select(attrs=attrs))
    restecg = forms.ChoiceField(label='Hasil Elektrokardiograf saat istirahat', choices=((-9, "Unknown"), (0,"Normal"), 
        (1,"Gelombang ST-T Abnormal"),(2,"Kemungkinan hipertrofi ventrikel kiri")), 
        widget=forms.Select(attrs=attrs))
    thalach = forms.ChoiceField(label='Maximum Heart Rate', choices=((-9, "Unknown"), (0,"< 150"), 
        (1,"150 < x < 160"), (2, "160 < x < 170"), (3, "170 < x < 180"), (4, "180 < x < 190"), 
        (5, "190 < x < 200"), (5, "200 ke atas")), widget=forms.Select(attrs=attrs))
    exang = forms.ChoiceField(label = 'Exercise Induced Angina', choices=((-9, "Unknown"), (1,"Yes"), (0,"No")), 
        widget=forms.Select(attrs=attrs))
    attrs.update({'placeholder' : 'Puncak ST Depression (isi -9 jika tidak tahu)'})
    oldpeak = forms.CharField(label='ST Depresi dari olahraga relatif terhadap istirahat', 
        widget=forms.TextInput(attrs=attrs))
    slope = forms.ChoiceField(label = 'Slope dari puncak exercise ST segment', choices=((-9, "Unknown"), (1,"Upsloping"), 
        (2,"Flat"), (3, "Downsloping")), widget=forms.Select(attrs=attrs))
    ca = forms.ChoiceField(label = 'Jumlah pembuluh major yang berwarna pada floroskopi', 
        choices=((-9, "Unknown"), (0,"0"), (1,"1"), (2, "2"), (3, "3")), widget=forms.Select(attrs=attrs))
    thal = forms.ChoiceField(label = 'Thallium Heart Scan', choices=((-9, "Unknown"), (3,"Normal"), (6,"Fixed Defect"), 
        (7, "Reversible Defect")), widget=forms.Select(attrs=attrs))
    
    
