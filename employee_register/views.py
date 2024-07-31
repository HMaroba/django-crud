from django.shortcuts import render
from employee_register.forms import EmployeeForm

# Create your views here.


def employee_list(request):
    return render(request, "employee_register/employee_list.html")

def employee_form(request):
    form = EmployeeForm
    return render(request, "employee_register/employee_form.html")

def employee_delete(request):
    return