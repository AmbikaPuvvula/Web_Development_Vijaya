from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sample(request):
	return HttpResponse("<h1>Welcome to django session</h1>")


def centerexample(request):
	return HttpResponse("<center> <h1>Welcome Archana</h1> </center>")

def paragraph(request):
	return HttpResponse("<p>Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.</p>")


def taskfun(request):
	return HttpResponse("<center><h1>Welcome to django session</h1></center><br><br><h1>Welcome Archana</h1><br><br><p>Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.</p>")

def stringvalueex(request,name):
	return HttpResponse("Helloooo......"+name)

def intvalueex(request,num):
	return HttpResponse("Age is.....%d"%num)

def samplehtmlex(request):
	return render(request,'student/sample.html')

def htmlexcss(request):
	return render(request,'student/demo.html')

def bootstrapex(request):
	return render(request,'student/bootstrapex.html')
def htmlex(request):
	return render(request,'student/s.html')




def login(request):
	return render(request,'student/login.html')


def register(request):
	if request.method == 'POST':
		Fname = request.POST.get('fname')
		Lname = request.POST.get('lname')
		Username = request.POST.get('username')
		Rollno = request.POST.get('rollno')
		Email = request.POST.get('email')
		Password = request.POST.get('password')
		Mobile = request.POST.get('mobile')
		#print(Fname,Lname,Username)
		return render(request,'student/details.html',{'Fname':Fname,'Lname':Lname,'Username':Username,'Rollno':Rollno,'Email':Email,'Password':Password,'Mobile':Mobile})
	return render(request,'student/register.html')
