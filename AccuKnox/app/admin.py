# employees/admin.py
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'job_title', 'department', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'job_title')
    list_filter = ('department', 'is_active')
    ordering = ('last_name', 'first_name')
    fields = ('email', 'first_name', 'last_name', 'phone_number', 'job_title', 'department',
              'date_of_birth', 'date_of_hire', 'salary', 'is_active', 'is_staff')
