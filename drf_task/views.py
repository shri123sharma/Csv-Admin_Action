from django.shortcuts import render
from .models import *
from .serilaizers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# Create your views here.

class HospitalView(APIView):

  def get(self, request, format=None):
      snippets = Hospital.objects.all()
      serializer = HospitalSerializer(snippets, many=True)
      return Response(serializer.data)

  def post(self, request, format=None):
      serializer = HospitalSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def put(self, request, pk, format=None):
        # import pdb;pdb.set_trace()
        snippet = Hospital.objects.get(Hos_id=pk)
        serializer = HospitalSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      snippet = Hospital.objects.get(Hos_id=pk)
      snippet.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  
class PatientView(APIView):

  def get(self, request, format=None):
      patient = Patient.objects.all()
      Patient_serializer = PatientSerializer(patient, many=True)
      return Response(Patient_serializer.data)

  def post(self, request, format=None):
      Patient_serializer = PatientSerializer(data=request.data)
      if Patient_serializer.is_valid():
          Patient_serializer.save()
          return Response(Patient_serializer.data, status=status.HTTP_201_CREATED)
      return Response(Patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def put(self, request, pk, format=None):
        # import pdb;pdb.set_trace()
        patient = Patient.objects.get(pat_id=pk)
        Patient_serializer = PatientSerializer(patient, data=request.data)
        if Patient_serializer.is_valid():
            Patient_serializer.save()
            return Response(Patient_serializer.data)
        return Response(Patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      patient = Patient.objects.get(pat_id=pk)
      patient.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  
class MedicalRecordView(APIView):

  def get(self, request, format=None):
      medical_record = MedicalRecord.objects.all()
      medical_serializer = MedicalRecordSerilaizer(medical_record, many=True)
      return Response(medical_serializer.data)

  def post(self, request, format=None):
      medical_serializer = MedicalRecordSerilaizer(data=request.data)
      if medical_serializer.is_valid():
          medical_serializer.save()
          return Response(medical_serializer.data, status=status.HTTP_201_CREATED)
      return Response(medical_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def put(self, request, pk, format=None):
        medical_record = Patient.objects.get(id=pk)
        medical_serializer = PatientSerializer(medical_record, data=request.data)
        if medical_serializer.is_valid():
            medical_serializer.save()
            return Response(medical_serializer.data)
        return Response(medical_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      medical_record = Patient.objects.get(id=pk)
      medical_record.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

