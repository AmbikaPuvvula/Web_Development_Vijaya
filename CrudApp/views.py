from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudApp.models import Student

# Create your views here.
def demo(request):
	return HttpResponse('From Crud App .....')

def home(request):
	return render(request,'CrudApp/home.html')


def addstudent(request):
	if request.method == 'POST':
		fn = request.POST.get('fname')
		ln = request.POST.get('lname')
		n = request.POST.get('name')
		r = request.POST.get('rollno')
		e = request.POST.get('email')
		m = request.POST.get('mobile')
		g = request.POST.get('gender')
		a = request.POST.get('age')
		Student.objects.create(fname=fn,lname=ln,
			name=n,rnum=r,email=e,
			mobile=m,gender=g,age=a)
		# return HttpResponse('Record Inserted Succesfully....')
		return redirect('details')
	return render(request,'CrudApp/addstudent.html')

def details(request):
	info = Student.objects.all()
	context = {'info':info}
	return render(request,'CrudApp/details.html',context)

def update(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.fname = request.POST['fname']
		data.lname = request.POST['lname']
		data.name = request.POST['name']
		data.rnum = request.POST['rollno']
		data.email = request.POST['email']
		data.mobile = request.POST['mobile']
		data.gender = request.POST['gender']
		data.age = request.POST['age']
		data.save()
		return redirect('details')
	return render(request,'CrudApp/update.html',{'data':data})

def delete(request,id):
	obj = Student.objects.get(id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('details')
	return render(request,'CrudApp/delete.html',{'obj':obj})