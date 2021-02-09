## Admin tables
	- python manage.py makemigrations
	- python manage.py migrate

## Admin page
	- have to create superuser
		- python manage.py createsuperuser

## CRUD Operations
	- Create new App
		- python manage.py startapp CrudApp
		- open settings.py file and Add app name in installedapps
		- open urls.py(project folder)
			- add include 
		- create new file in CrudApp rename as `urls.py` 

 fname
 lname
 name
 rnum
 email
 mobile
 gender
 age



 Create
  classname.objects.create('fieldname'= value)
 Read
 classname.objects.all()
 classname.objects.get(id)
 classname.objects.filter()
 Update
 classname.objects.get()
 save()
 delete
 classname.objects.delete()




 templates
 	folder
 		htmlpages