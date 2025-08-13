
import os
import pickle
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import logout
# Load models
BASE_DIR = settings.BASE_DIR
MODEL_DIR = os.path.join(BASE_DIR, 'predictor', 'models')

diabetes_model = pickle.load(open(os.path.join(MODEL_DIR, 'diabetes_model.sav'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(MODEL_DIR, 'heart_disease_model.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(MODEL_DIR, 'parkinsons_model.sav'), 'rb'))

def home(request):
    return render(request, 'predictor/home.html')

def diabetes_predict(request):
    result = None
    if request.method == 'POST':
        data = [
            float(request.POST['Pregnancies']),
            float(request.POST['Glucose']),
            float(request.POST['BloodPressure']),
            float(request.POST['SkinThickness']),
            float(request.POST['Insulin']),
            float(request.POST['BMI']),
            float(request.POST['DiabetesPedigreeFunction']),
            float(request.POST['Age']),
        ]
        prediction = diabetes_model.predict([data])
        result = 'Positive' if prediction[0] == 1 else 'Negative'
    return render(request, 'predictor/diabetes.html', {'result': result})


def heart_predict(request):
    result = None
    if request.method == 'POST':
        data = [
            float(request.POST['age']),
            float(request.POST['sex']),
            float(request.POST['cp']),
            float(request.POST['trestbps']),
            float(request.POST['chol']),
            float(request.POST['fbs']),
            float(request.POST['restecg']),
            float(request.POST['thalach']),
            float(request.POST['exang']),
            float(request.POST['oldpeak']),
            float(request.POST['slope']),
            float(request.POST['ca']),
            float(request.POST['thal']),
        ]
        prediction = heart_disease_model.predict([data])
        result = 'Positive' if prediction[0] == 1 else 'Negative'
    return render(request, 'predictor/heart.html', {'result': result})


def parkinsons_predict(request):
    result = None
    if request.method == 'POST':
        features = [
            float(request.POST['MDVP:Fo(Hz)']),
            float(request.POST['MDVP:Fhi(Hz)']),
            float(request.POST['MDVP:Flo(Hz)']),
            float(request.POST['MDVP:Jitter(%)']),
            float(request.POST['MDVP:Jitter(Abs)']),
            float(request.POST['MDVP:RAP']),
            float(request.POST['MDVP:PPQ']),
            float(request.POST['Jitter:DDP']),
            float(request.POST['MDVP:Shimmer']),
            float(request.POST['MDVP:Shimmer(dB)']),
            float(request.POST['Shimmer:APQ3']),
            float(request.POST['Shimmer:APQ5']),
            float(request.POST['MDVP:APQ']),
            float(request.POST['Shimmer:DDA']),
            float(request.POST['NHR']),
            float(request.POST['HNR']),
            float(request.POST['RPDE']),
            float(request.POST['DFA']),
            float(request.POST['spread1']),
            float(request.POST['spread2']),
            float(request.POST['D2']),
            float(request.POST['PPE']),
        ]
        prediction = parkinsons_model.predict([features])
        result = 'Positive' if prediction[0] == 1 else 'Negative'

    return render(request, 'predictor/parkinsons.html', {'result': result})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'predictor/home.html')

def logout_view(request):
    logout(request)
    return redirect('login') 