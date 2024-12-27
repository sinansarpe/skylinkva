from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import (CustomUser, 
                    #UserImageContent, UserTextContent, 
                    #RecommendCategory, Recommend
                    )


from app_airline.models import StaffPositions
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model           = CustomUser
    list_display    = ("email", "is_staff", "is_active",)
    list_filter     = ("is_pilot", "is_vastaff", "is_staff", "is_active",)
    fieldsets       = (
                        ("USER", {"fields": ("email", "username","first_name","last_name","age", "password", "last_login", "date_joined","activation_date")}),
                        ("PROFILE", {
                            "fields":("profile_image", "division_name", "ivao_id","apply_for_pilot","is_invitation_sent", "vamsys_id","is_pilot","pilot_title","is_onTrial")}),
                        #("BADGES",{
                        #    "fields":("iatc_title",
                        #                       ,"ipilot_title", "apilot_title",
                        #    )}),    
                        ("STAFF MANAGEMENT", {
                            "fields":("is_vastaff","staff_title",)}),
                        ("GROUPS AND PERMISSIONS", {
                            "fields": ("is_staff", "is_active", "groups", "user_permissions")}),
                        )
    
    add_fieldsets   = (
                        (None, {
                            "classes": ("wide",),
                            "fields": (
                                "email", "username", "password1", "password2", "is_staff",
                                "is_active", "groups", "user_permissions"
                            )}
                        ),
                    )
    
    search_fields   = ("username",)
    ordering        = ("email",)
    list_display    = ["email", "username","first_name","last_name","apply_for_pilot", "ivao_id", "vamsys_id", "is_pilot","is_onTrial"]

admin.site.register(CustomUser, CustomUserAdmin)

'''
class iATCBadgesAdmin (admin.ModelAdmin):
    pass

admin.site.register(iATCBadges, iATCBadgesAdmin)


class UserImageContentAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserImageContent, UserImageContentAdmin)

class UserTextContentAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(UserTextContent, UserTextContentAdmin)



class  RecommendCategoryAdmin (admin.ModelAdmin):
    pass
admin.site.register(RecommendCategory, RecommendCategoryAdmin)

class RecommendAdmin (admin.ModelAdmin):
    pass
admin.site.register(Recommend, RecommendAdmin)
'''