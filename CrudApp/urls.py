from django.urls import path
from CrudApp import views

urlpatterns =[
	path('demo1/',views.demo),
	path('',views.home,name='home'),
	path('addstudent/',views.addstudent,name='addstudent'),
	path('details/',views.details,name='details'),
	path('update/<int:id>',views.update,name='update'),
	path('delete/<int:id>',views.delete,name='delete'),
]