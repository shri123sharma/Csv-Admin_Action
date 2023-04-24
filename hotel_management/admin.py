from django.contrib import admin
from hotel_management.models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer_id','customer_name','customer_email','customer_address','status']
admin.site.register(Customer,CustomerAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display=['payment_id','payment_customer','payment_date']
admin.site.register(Payment,PaymentAdmin)

class EmployeesAdmin(admin.ModelAdmin):
    list_display=['employee_id','job_department','employee_address','contact_add']
    fieldsets=(
    ('Login_Info',{'fields':('username','password','first_name','last_name','email')}),
    ('Employee_Info',{'fields':('job_department','employee_address','contact_add')}),
    )

admin.site.register(Employees,EmployeesAdmin)

class RoomClassAdmin(admin.ModelAdmin):
    list_display=['class_id','room_name']
admin.site.register(RoomClass,RoomClassAdmin)

class RoomInformationAdmin(admin.ModelAdmin):
    list_display=['room_id','class_id','description','price']
admin.site.register(RoomInformation,RoomInformationAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display=['reservation_id','customer_id','room_id','reservation_date','date_in','date_out','date_range',]
admin.site.register(Reservation,ReservationAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=['transaction_id','transaction_name','customer_id','payment_id','employee_id','reservation_id','transaction_date',]
admin.site.register(Transaction,TransactionAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display=['report_id','transaction_id','information','date']
admin.site.register(Report,ReportAdmin)








