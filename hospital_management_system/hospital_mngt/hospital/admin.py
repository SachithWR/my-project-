from django.contrib import admin

from hospital_mngt.hospital.models import Appoinment, Doctor, Patient

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinment)