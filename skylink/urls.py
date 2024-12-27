"""
URL configuration for skylink project.

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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ContactFormView

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('captcha/', include('captcha.urls')),

    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    
    path('u/', include('app_users.urls'), name=""),
    path('a/', include('app_airline.urls'), name=""),
    path('c/', include('app_community.urls'), name=""),
    path('o/', include('app_staff.urls'), name=""),
    path('g/', include('app_gallery.urls'), name=""),
    path('contact/', ContactFormView.as_view(), name='contact'),


    #path('test/',views.vamsys_pilot, name="test" ),
    #path('ltfe/',views.airport, name="ltfe" ),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# CONFIGURE ADMIN TITLES
admin.site.site_header = "SKYLINK Administration Page"
admin.site.site_title = "SKYLINK"
admin.site.index_title = "Welcome to SKYLINK Administration Page"