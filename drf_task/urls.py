from .views import *
from django import views
from django.urls import path

urlpatterns=[
    
    path('hospital/',HospitalView.as_view(),name='hospital'),
    path('hospital/<int:pk>/',HospitalView.as_view(),name='hospital'),
    path('patient/',PatientView.as_view(),name='patient'),
    path('patient/<int:pk>/',PatientView.as_view(),name='patient'),
    path('medical_record/',MedicalRecordView.as_view(),name='medical_record'),
    path('medical_record/<int:pk>/',MedicalRecordView.as_view(),name='medical_record'),
    
]