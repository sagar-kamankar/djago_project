"""
URL configuration for MySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from MySite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage,name="home"),
    path("about-us/",views.aboutUs,name="about"),
    path("Services/",views.services,name="services"),
    path("Contact/",views.contact,name='contact'),
    path("saveenquiry",views.saveEnquiry,name="saveenquiry"),
    path("Course-Name/<str:coursename>",views.courseName),
    path("Slug-Url/<slug:name>",views.slugUrl),
    path("Student-name/<str:studentname>/<str:coursename>",views.studentname),
    path("Userform/",views.userForm),
    path("submitform/",views.submitform,name="submitform"),
    path("calculator/",views.calculator,name="calculator"),
    path("checknumber",views.checknumber,name="checknumber"),
    path("marksheet",views.marksheet,name="marksheet"),
    path("newsDetails/<slug>",views.newsDetails),



]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
