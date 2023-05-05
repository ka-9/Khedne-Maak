"""
URL configuration for kmweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from frontend import views


urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.home, name='home'),
     path('signin/', views.signin, name='signin'),
     path('signup/', views.signup, name='signup'),
     path('signout/', views.signout, name='signout'),
     path('signout/', views.signout, name='signout'),
     path('create_ride', views.create_ride, name='create_ride'),
     path('ride/<int:ride_id>/', views.ride_detail, name='ride_detail'),
     path('join-ride/', views.join_ride, name='join_ride')
    
 ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)