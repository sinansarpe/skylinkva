from django.urls import path, re_path

from django.contrib.auth import views as auth_views

from . import views 
from .views import (
                        ResetPasswordView, 
                        CustomPasswordResetConfirmView, 
                        CustomPasswordResetCompleteView,

                        password_reset_success 
                        #, UserProfile

                        )       
urlpatterns = [
        
        path('login/',views.signin, name = 'signin'),
        path('logout/', views.signout, name = 'signout'),
        path('signup', views.signup, name='signup'),
        path('activate/<uidb64>/<token>/',views.activate, name='activate'),
        path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
        path('new-pasword/', views.password_reset_success, name='password_reset_success'),
        path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),name='password_reset_confirm'),    
        path('password-reset-complete/', CustomPasswordResetCompleteView.as_view(),name='password_reset_complete'),


        #path('profil-olustur/', views.create_profile, name='create_profile'),
        #path('profil-form/', views.edit_profile, name='profile-edit'),

        #path('dashboard/', views.dashboard, name = 'dashboard'),
        #path('pilot-application/', views.pilot_application, name='pilot_application'),
        #path('pilot-hired/<int:id>/', views.pilot_hired, name='pilot_hired'),
        #path('pilot-hired/', views.pilot_hired, name='pilot_hired'),
#        path('delete_image/<int:id>/', views.delete_image, name='delete_image'),

    ]