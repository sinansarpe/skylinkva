from django.contrib import admin

from .models import UploadLivery
# Register your models here.

class UploadLiveryAdmin (admin.ModelAdmin):
    pass

admin.site.register(UploadLivery, UploadLiveryAdmin)