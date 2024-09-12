# employees/forms.py
from django import forms
from .models import Employee

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'email', 'first_name', 'last_name', 'phone_number',
            'job_title', 'department', 'date_of_birth', 'date_of_hire', 'salary'
        ]
