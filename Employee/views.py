from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def employee_list(request):
    employee1 = Employee.objects.all()
    return render(request,template_name='employee_list.html',context={'employees': employee1})

def employee_details(request, id):
    employee2 = get_object_or_404(Employee, id=id)
    return render(request,template_name='employee_details.html',context={'employees': employee2})

def employee_create(request):
    if request.method == 'POST':
        name1 = request.POST['name']
        email1 = request.POST['email']
        age1 = request.POST['age']
        Employee.objects.create(name=name1,email=email1,age=age1)
        return redirect('employee_list')

    return render(request,template_name='employee_form.html')

def employee_update(request, id):
    employee3 = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        employee3.name = request.POST['name']
        employee3.email = request.POST['email']
        employee3.age = request.POST['age']
        employee3.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'employee': employee3})

def employee_delete(request,id):
    employee4 = get_object_or_404(Employee,id=id)
    if request.method=="POST":
        employee4.delete()
        return redirect('employee_list')
    return render(request,template_name='employee_confirm_delete.html',context={'employees':employee4})
        


# Create your views here.