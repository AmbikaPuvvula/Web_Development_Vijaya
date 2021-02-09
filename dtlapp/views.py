from django.shortcuts import render,redirect

from dtlapp.forms import Userreg
from django.contrib import messages
# Create your views here.


def home(request):
	return render(request,'dtlapp/home.html')

def about(request):
	return render(request,'dtlapp/about.html')

def contact(request):
	return render(request,'dtlapp/contact.html')

def dashboard(request):
	return render(request,'dtlapp/dashboard.html')

def login(request):
	return render(request,'dtlapp/login.html')


def register(request):
	if request.method == 'POST':
		data=Userreg(request.POST)
		if data.is_valid():
			data.save()
			messages.success(request,"successfully Registered")
			#redirect('login')
	data=Userreg()
	return render(request,'dtlapp/register.html',{'data':data})