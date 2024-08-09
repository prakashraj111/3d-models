from django.contrib import admin
from myapp.models import Student, Customer, BloodRequest


admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(BloodRequest)
# Register your models here.

