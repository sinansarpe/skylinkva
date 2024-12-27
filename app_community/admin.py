from django.contrib import admin
from .models import Screenshots

# Register your models here.

class ScreenshotsAdmin (admin.ModelAdmin):

    list_display        = ['username','is_published','is_featured','is_mainpage','uploaded_at']

admin.site.register(Screenshots, ScreenshotsAdmin)

