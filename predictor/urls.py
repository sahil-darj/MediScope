from django.urls import path
from . import views

urlpatterns = [
    path('diabetes/', views.diabetes_predict, name='diabetes_predict'),
    path('heart/', views.heart_predict, name='heart_predict'),
    path('parkinsons/', views.parkinsons_predict, name='parkinsons_predict'),
    path('signup/', views.signup_view, name='signup'),
]
