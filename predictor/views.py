# predictor/views.py

import os
import pandas as pd
import joblib
from django.shortcuts import render
from django.conf import settings
from .forms import HeartDiseaseForm


# Load model and preprocessing components
model_path = os.path.join(settings.ML_MODELS_DIR, 'heart_disease_predictor.pkl')
scaler_path = os.path.join(settings.ML_MODELS_DIR, 'scaler.pkl')
feature_names_path = os.path.join(settings.ML_MODELS_DIR, 'feature_names.pkl')

# Check if model files exist, otherwise use placeholders for development
try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature_names = joblib.load(feature_names_path)
except FileNotFoundError:
    # This is just for development, before you've moved your trained models
    # In a real app, you'd handle this differently
    model = None
    scaler = None
    feature_names = None
    print("Warning: ML model files not found. Prediction will not work correctly.")

def index(request):
    """View for the home page with the prediction form."""
    form = HeartDiseaseForm()
    return render(request, 'predictor/index.html', {'form': form})

def predict(request):
    """View to process the form data and make predictions."""
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            # Get cleaned data from form
            patient_data = {
                'Age': int(form.cleaned_data['age']),
                'Sex': form.cleaned_data['sex'],
                'ChestPainType': form.cleaned_data['chest_pain_type'],
                'RestingBP': int(form.cleaned_data['resting_bp']),
                'Cholesterol': int(form.cleaned_data['cholesterol']),
                'FastingBS': int(form.cleaned_data['fasting_bs']),
                'RestingECG': form.cleaned_data['resting_ecg'],
                'MaxHR': int(form.cleaned_data['max_hr']),
                'ExerciseAngina': form.cleaned_data['exercise_angina'],
                'Oldpeak': float(form.cleaned_data['oldpeak']),
                'ST_Slope': form.cleaned_data['st_slope'],
            }
            
            # Create DataFrame from patient data
            input_df = pd.DataFrame([patient_data])
            
            if model is not None and scaler is not None and feature_names is not None:
                # Preprocessing steps
                # 1. Binary encoding
                # At the start of your predict view
                print("Model loaded:", model is not None)
                print("Scaler loaded:", scaler is not None)
                print("Feature names loaded:", feature_names is not None if feature_names else "None")
                input_df['Sex'] = input_df['Sex'].map({'M': 1, 'F': 0})
                input_df['ExerciseAngina'] = input_df['ExerciseAngina'].map({'Y': 1, 'N': 0})
                
                # 2. One-hot encoding
                input_encoded = pd.get_dummies(input_df, columns=['ChestPainType', 'RestingECG', 'ST_Slope'], drop_first=True)
                
                # Ensure all feature columns are present
                for feature in feature_names:
                    if feature not in input_encoded.columns:
                        input_encoded[feature] = 0
                
                # Keep only needed columns in correct order
                input_final = input_encoded[feature_names]
                
                # 3. Feature scaling
                numerical_features = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
                input_final[numerical_features] = scaler.transform(input_final[numerical_features])
                
                # Make prediction
                prediction = int(model.predict(input_final)[0])
                probability = float(model.predict_proba(input_final)[0][1])
                
                # Determine risk level
                if probability < 0.3:
                    risk_level = "Low Risk"
                    risk_class = "low-risk"
                elif probability < 0.7:
                    risk_level = "Moderate Risk"
                    risk_class = "moderate-risk"
                else:
                    risk_level = "High Risk"
                    risk_class = "high-risk"
            else:
                # Sample predictions for development (when model files aren't available)
                prediction = 1
                probability = 0.75
                risk_level = "High Risk"
                risk_class = "high-risk"
                
            # Format probability as percentage
            probability_percent = f"{probability:.2%}"
            
            # Create context for template
            context = {
                'form': form,
                'prediction': prediction,
                'probability': probability_percent,
                'risk_level': risk_level,
                'risk_class': risk_class,
                'has_heart_disease': "Yes" if prediction == 1 else "No",
                'submitted': True
            }
            
            return render(request, 'predictor/index.html', context)
    else:
        form = HeartDiseaseForm()
    
    return render(request, 'predictor/index.html', {'form': form})
