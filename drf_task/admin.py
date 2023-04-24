from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Doctor)