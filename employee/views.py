from django.shortcuts import render
from .models import Employee
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request,'employee/index.html',{'employees': Employee.objects.all()})
    

def E_employee(request,id):
    employee = Employee.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    if form.is_valid():
      new_employee_number = form.cleaned_data['employee_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_department = form.cleaned_data['department']
      new_salary = form.cleaned_data['salary']

      new_employee = Employee(
        employee_number = new_employee_number,
        first_name = new_first_name,
        last_name = new_last_name,
        email = new_email,
       department = new_department,
        salary = new_salary
      )
      new_employee.save()
      return render(request, 'employee/add.html', {
        'form': EmployeeForm(),
        'success': True
      })
  else:
    form = EmployeeForm()
  return render(request, 'employee/add.html', {
    'form': EmployeeForm()
  }) 


def edit(request, id):
  if request.method == 'POST':
    employee = Employee.objects.get(pk=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
      form.save()
      return render(request, 'employee/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Employee.objects.get(pk=id)
    form = EmployeeForm(instance=student)
  return render(request, 'employee/edit.html', {
    'form': form
  })
def delete(request, id):
  if request.method == 'POST':
    employee = Employee.objects.get(pk=id)
    employee.delete()
  return HttpResponseRedirect(reverse('index'))