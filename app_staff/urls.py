from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import LiveryDeleteView #, delete_livery

urlpatterns = [

        path('office/', views.office_page, name = 'office'),
        path('office/screenshots/', views.approve_screenshots, name='approve_screenshots'),
        path('office/screenshots/approved/<int:id>/', views.ss_approved, name='ss_approved'),
        
        path('office/applicants/', views.applicants, name="applicants"),
        path('office/applicants/invited/<int:id>/', views.invited, name='invited'),

        path('office/upload-livery/', views.upload_livery_view, name='upload_livery'),

        #path('office/applicants/assignvamsysid/<int:user_id>', views.assign_vamsysID, name='vamsysid'),

        path('livery/<int:pk>/delete/', LiveryDeleteView.as_view(), name='livery_delete'),

        # Function-based view:
        #path('livery/<int:pk>/delete-fbv/', delete_livery, name='livery_delete_fbv'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)