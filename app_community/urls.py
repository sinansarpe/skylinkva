from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import DeleteAccountView, delete_account

urlpatterns = [

        path('dashboard/', views.dashboard, name = 'dashboard'),
        
        path('dashboard/screenshots/', views.screenshots_form, name='screenshots_form'),
        path('delete_screenshot/<int:id>/', views.delete_image, name='delete_image'),
        path('delete_published/<int:id>/', views.delete_published, name='delete_published'),
        
        path('dashboard/delete-account/', views.delete_account, name='delete_account'),
        path('dashboard/delete-account_confirmed/', DeleteAccountView.as_view(), name='delete_account_confirmed'),

        path('pilot-application/', views.pilot_application, name='pilot_application'),
        path('pilot-hired/<int:id>/', views.pilot_hired, name='pilot_hired'),

        path('dashboard/download-livery/', views.downloadLivery, name='download_livery'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)