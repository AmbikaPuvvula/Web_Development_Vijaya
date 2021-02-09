from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Userreg(UserCreationForm):
	password1=forms.CharField(widget=(forms.PasswordInput(attrs=
		{'class':'form-control','placeholder':'enter password'})
		))
	password2=forms.CharField(widget=(forms.PasswordInput(attrs=
		{'class':'form-control','placeholder':'enter confirm pass'})))

	class Meta:
		model = User
		fields = ['username','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'example@gmail.com'})
		}
