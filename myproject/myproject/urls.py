"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from members import views
from members.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path("login",views.login1,name="login"),
    
    path("register",views.register,name="register"),
    path("signup1",views.signup_o,name="signup1"),
    path("signup2",views.signup_u,name="signup2"),
    path("organizers",views.org_1,name="organizers"),
    path("table",views.table,name="table"),
     path("dashboard1",views.dashboard1,name="dashboard1"),
     path("person_detail",views.person_detail,name="person_detail"),
     path("dashboard2",views.dashboard2,name="dashboard2"),
     path("logout",views.logout,name="logout"),
     path("event_details",event_details,name="event_details"),
     path("o_profile",views.o_profile,name="o_profile"),
     path("u_profile",views.u_profile,name="u_profile"),
     path("book",views.books,name="book"),
     path("bookings",views.bookings,name="bookings"),
     path("about",views.about,name="about"),
      path("contact",views.about,name="contact")
     

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
