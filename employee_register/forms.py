from django import forms # type: ignore
from .models import Employee


class EmployeeForm(forms.ModelForm):


    class Meta:
        model = Employee
        fields = '_all_'



