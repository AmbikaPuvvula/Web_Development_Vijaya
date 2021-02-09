from django.urls import path
from dtlapp import views
urlpatterns=[
path('home/',views.home,name='home'),
path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),
path('dsh/',views.dashboard,name='dsh'),
path('login/',views.login,name='login'),
path('register/',views.register,name='register'),
]