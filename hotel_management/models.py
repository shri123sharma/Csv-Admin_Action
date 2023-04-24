from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True,null=False,blank=False)
    customer_name=models.CharField(max_length=255,null=False,blank=False)
    customer_email=models.EmailField(max_length=255,null=False,blank=False)
    customer_address=models.CharField(max_length=255,null=False,blank=False)
    status=models.BooleanField(default=False)

    def __str__(self):
      return self.customer_name
    
class Payment(models.Model):
   payment_id=models.AutoField(primary_key=True,null=False,blank=False)
   payment_customer=models.ForeignKey(Customer,null=True,blank=True,related_name='customer_payment',on_delete=models.CASCADE)
   payment_date=models.DateField(auto_now_add=True)

   def __str__(self):
      return str(self.payment_customer)
   
class Employees(User):
   employee_id=models.AutoField(primary_key=True,null=False,blank=False)
   job_department=models.CharField(max_length=255,null=False,blank=False)
   employee_address=models.CharField(max_length=255,null=False,blank=False)
   contact_add=models.PositiveIntegerField(default='+914434232322',null=False,blank=False)

   class Meta:
      verbose_name = "Employees"
      verbose_name_plural = "Employees"

   def __str__(self):
      return self.first_name+"-"+self.job_department
   
class RoomClass(models.Model):
   class_id=models.AutoField(primary_key=True,blank=False,null=False)
   room_name=models.CharField(max_length=255,null=False,blank=False)

   def __str__(self):
    return self.room_name
   
class RoomInformation(models.Model):
   room_id=models.AutoField(primary_key=True,null=False,blank=False)
   class_id=models.ForeignKey(RoomClass,null=True,blank=True,related_name='roomclass_roominformation',on_delete=models.CASCADE)
   description=models.TextField()
   price=models.PositiveIntegerField()

   def __str__(self):
    return self.description
   
class Reservation(models.Model):
   reservation_id=models.AutoField(primary_key=True,null=False,blank=False)
   customer_id=models.ForeignKey(Customer,null=True,blank=True,related_name='customer_reservation',on_delete=models.CASCADE)
   room_id=models.ForeignKey(RoomInformation,null=True,blank=True,related_name='roominformation_reservation',on_delete=models.CASCADE)
   reservation_date=models.DateTimeField(auto_now_add=True)
   date_in=models.DateField()
   date_out=models.DateField()
   date_range=models.DateField()

   def __str__(self):
      return str(self.reservation_date) 
   
class Transaction(models.Model):
   transaction_id=models.AutoField(primary_key=True,null=False,blank=False)
   transaction_name=models.CharField(max_length=255,null=False,blank=False)
   customer_id=models.ForeignKey(Customer,null=True,blank=True,related_name='customer_transaction',on_delete=models.CASCADE)
   payment_id=models.ForeignKey(Payment,null=True,blank=True,related_name='payment_transaction',on_delete=models.CASCADE)
   employee_id=models.ForeignKey(Employees,null=True,blank=True,related_name='employee_transaction',on_delete=models.CASCADE)
   reservation_id=models.ForeignKey(Reservation,null=True,blank=True,related_name='reservation_transaction',on_delete=models.CASCADE)
   transaction_date=models.DateField(auto_now_add=True)

   def __str__(self):
      return self.transaction_name
   
class Report(models.Model):
   report_id=models.AutoField(primary_key=True,null=False,blank=False)
   transaction_id=models.ForeignKey(Transaction,null=True,blank=True,related_name='transaction_report',on_delete=models.CASCADE)
   information=models.CharField(max_length=255,null=False,blank=False)
   date=models.DateField(auto_created=True)

   def __str__(self):
      return self.information
   

   



   

