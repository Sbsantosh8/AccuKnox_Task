# employees/views.py
from django.shortcuts import render, redirect
from .forms import EmployeeRegistrationForm
from .models import Employee
from django.http import HttpResponse
import threading
import logging

logger = logging.getLogger(__name__)

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            logger.info("Before Saving ...")
            print(f"Signal Caller thread ID: {threading.get_ident()}")

            form.save()  # This triggers the post_save signal
            logger.info("After Saving....")
            return HttpResponse('Employee Registered  Successfully!! ')
    else:
        form = EmployeeRegistrationForm()

    return render(request, 'register.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


