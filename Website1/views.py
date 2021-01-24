from django.shortcuts import render,redirect

# Create your views here.
from Website1.forms import EmployeeForm
from Website1.models import Employee

def show_view(request):
	employees=Employee.objects.all()
	return render(request,'Website1/index.html',{'employees':employees})

def insert_view(request):
	form=EmployeeForm()
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'Website1/insert.html',{'form':form})


def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/')

def update_view(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=='POST':
		form=EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'Website1/update.html',{'employee':employee})