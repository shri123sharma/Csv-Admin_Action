from django.db import models

# Create your models here.
class Hospital(models.Model):
  Hos_id=models.AutoField(primary_key=True,null=False,blank=False)
  Hos_name=models.CharField(max_length=255,null=False,blank=False)
  Hos_address=models.CharField(max_length=255,null=False,blank=False)
  Hos_city=models.CharField(max_length=255,null=False,blank=False)
  
  def __str__(self):
    return self.Hos_name
  
class Patient(models.Model):
  pat_hos=models.ForeignKey(Hospital,null=True,blank=True,related_name='hospital_patent',on_delete=models.CASCADE)
  pat_id=models.AutoField(primary_key=True,null=False, blank=False)
  pat_email=models.EmailField(max_length=255,null=False,blank=False,unique=True)
  pat_name=models.CharField(max_length=255,null=False,blank=False)
  pat_date_of_birth=models.DateField()
  pat_diagnosis=models.CharField(max_length=255,null=False,blank=False)
  pat_address=models.CharField(max_length=255,null=False,blank=False)

  def __str__(self):
    return self.pat_name
  
class MedicalRecord(models.Model):
  med_pat=models.ForeignKey(Patient,null=True,blank=True,related_name='patient_medical',on_delete=models.CASCADE)
  record_id=models.AutoField(primary_key=True,null=False,blank=False)
  date_of_exmaination=models.DateField(auto_now_add=True)
  problem=models.CharField(max_length=255,null=False,blank=False)

  def __str__(self):
    return self.problem+"--"+str(self.date_of_exmaination)
  
class Doctor(models.Model):
  doc_hos=models.ForeignKey(Hospital,null=True,blank=True,related_name='hospital_doctor',on_delete=models.CASCADE)
  doc_id=models.AutoField(primary_key=True,null=False,blank=False)
  doc_name=models.CharField(max_length=255,null=False,blank=False)
  doc_email=models.CharField(max_length=255,null=False,blank=False,unique=True)
  qualifcation=models.CharField(max_length=255,null=False,blank=False)
  salary=models.PositiveIntegerField(blank=False)

  def __str__(self):
    return self.doc_name
  
