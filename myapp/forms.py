from django import forms
from .models import Student , BloodRequest

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class bloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['title', 'blood_group', 'patient_name', 'hospital_name', 'contact_number', 'requirement_date', 'requirement_reason']         