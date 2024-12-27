from django.urls import path, re_path
from . import views



urlpatterns = [
                path('roster/', views.Roster, name='roster'),                
                path('staff/', views.Staffs, name='staff'),
                path('resources/', views.resources, name = 'resources'),
                path('resources/rules/', views.rules, name='rules'),
                path('resources/ranking/', views.ranking, name='ranking'),
                path('resources/operations/', views.flightops, name='flightops'),
                path('resources/privacy-policy/', views.privacy, name='privacy'),
                path('resources/faq/', views.faq , name="faq"),                

    ]