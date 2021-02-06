"""VitwProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',views.sample),
    path('center/',views.centerexample),
    path('paragraphex/',views.paragraph),
    path('task/',views.taskfun),
    path('stringvalue/<str:name>/',views.stringvalueex),
    path('intvalue/<int:num>/',views.intvalueex),
    path('samplehtml/',views.samplehtmlex,name=''),
    path('demo/',views.htmlexcss,name=''),
    path('s/',views.htmlex),
    path('bootex/',views.bootstrapex,name=''),
    path('loginpage/',views.login,name=''),
    path('registerpage/',views.register,name=''),
    path('',include('CrudApp.urls')),
    path('forms/',include('FormsApp.urls')),

]
