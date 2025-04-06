# predictor/forms.py

from django import forms

from django import forms


class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(min_value=18, max_value=100, 
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                           widget=forms.Select(attrs={'class': 'form-control'}))
    
    chest_pain_type = forms.ChoiceField(
        choices=[('ATA', 'Typical Angina'), ('NAP', 'Atypical Angina'), 
                ('ASY', 'Asymptomatic'), ('TA', 'Non-Anginal Pain')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    resting_bp = forms.IntegerField(min_value=80, max_value=200,
                                   widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    cholesterol = forms.IntegerField(min_value=100, max_value=600,
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    fasting_bs = forms.ChoiceField(
        choices=[(1, 'Yes (> 120 mg/dl)'), (0, 'No (≤ 120 mg/dl)')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    resting_ecg = forms.ChoiceField(
        choices=[('Normal', 'Normal'), ('ST', 'ST-T Wave Abnormality'), ('LVH', 'Left Ventricular Hypertrophy')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    max_hr = forms.IntegerField(min_value=60, max_value=220,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    exercise_angina = forms.ChoiceField(
        choices=[('Y', 'Yes'), ('N', 'No')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    oldpeak = forms.FloatField(min_value=0, max_value=10,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    st_slope = forms.ChoiceField(
        choices=[('Up', 'Upsloping'), ('Flat', 'Flat'), ('Down', 'Downsloping')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
