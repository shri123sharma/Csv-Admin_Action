from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator

class HospitalSerializer(serializers.Serializer):
    # import pdb;pdb.set_trace()
    Hos_name=serializers.CharField(max_length=255,)
    Hos_address=serializers.CharField(max_length=255)
    Hos_city=serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        return Hospital.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Hos_name = validated_data.get('Hos_name', instance.Hos_name)
        instance.Hos_address = validated_data.get('Hos_address', instance.Hos_address)
        instance.Hos_city = validated_data.get('Hos_city', instance.Hos_city)
        instance.save()
        return instance
    
# class HospitalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Hospital
#         fields=['hos_id','hos_name','hos_address','hos_city']

class PatientSerializer(serializers.ModelSerializer):
    pat_hos=serializers.SerializerMethodField()
    class Meta:
        model=Patient
        fields=['pat_hos','pat_name','pat_email','pat_date_of_birth','pat_diagnosis','pat_address']
        # depth = 1

    def get_pat_hos(self,obj):
        hospital=Hospital.objects.filter(hospital_patent__pat_id=obj.pat_id)
        if hospital:
          return HospitalSerializer(hospital,many=True).data
        
    def validate_pat_date_of_birth(self, value):
      from datetime import date
      today = date.today()
      age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
      if (not(20 < age < 30)):
        raise serializers.ValidationError("You are no eligible for the job")
      return value
   
class MedicalRecordSerilaizer(serializers.ModelSerializer):
    med_pat=serializers.SerializerMethodField()
    class Meta:
        model=MedicalRecord
        fields=['med_pat','date_of_exmaination','problem']

    def get_med_pat(self,obj):
        patient=Patient.objects.filter(patient_medical__record_id=obj.record_id)
        if patient:
            return PatientSerializer(patient,many=True).data
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=['doc_hos','doc_id','doc_name','qualifcation','salary']

