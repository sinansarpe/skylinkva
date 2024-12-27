from django.db import models
from django.conf import settings
from typing import Any
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save


from app_database.models import (
                                    Networks, 
                                    Divisions,
                                    ATCBadges,
                                    PilotBadges,
                                    
                                 ) 
from app_airline.models import  (
                                    AirlineBadges,
                                    StaffPositions,

                                )

#from airline import settings
#from airline_db.models import StaffPositions,ActiveDivisions, aPilotBadges
#from .validators import ValidationError


#https://testdriven.io/blog/django-custom-user-model/

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

    email               = models.EmailField     (_("email"), unique=True)
    username            = models.CharField      (_("username"), unique=True, max_length=12,
                                                    validators=[
                                                        MinLengthValidator(4, 'Username must be 4 to 12 characters long.')]
                                                )
    first_name          = models.CharField      ('First Name', max_length=50, null=True, blank=True)
    last_name           = models.CharField      ('Last Name', max_length=50, null=True, blank=True)
    age                 = models.DateField      ('Date of Birth', null=True, blank=True)
    activation_date     = models.DateTimeField  (null=True, blank=True)

    apply_for_pilot     = models.BooleanField   ('Applicant for Pilot', default=False)
    pilots_info_checked = models.BooleanField   ('Checked Pilot Info', default=False )
    is_invited_vamsys   = models.DateTimeField  ('Invited to vaMSYS Date', null=True, blank=True, auto_now_add=True)
    

    division_name       = models.ForeignKey     (Divisions, on_delete=models.CASCADE, null=True, blank=True)
    ivao_id             = models.CharField      ('IVAO ID (VID)', max_length=7, unique=True, null=True, blank=True)
    vamsys_id           = models.CharField      ('vaMSYS ID', max_length=20, unique=True, null=True, blank=True)

    profile_image       = models.ImageField     ('Profile Picture', upload_to='members/uploads/profile/image', null=True, blank=True)
    is_invitation_sent  = models.BooleanField   ('Invitation Sent', default=False)
    is_pilot            = models.BooleanField   ('Airline Pilot', default=False)
    pilot_title         = models.ForeignKey     (AirlineBadges, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Pilot Rank')
    is_vastaff          = models.BooleanField   ('Airline Staff', default=False)
    is_onTrial          = models.BooleanField   ('is on Trial', default=True)
    staff_title         = models.ForeignKey     (StaffPositions, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Staff Position')

    USERNAME_FIELD      = "email"
    REQUIRED_FIELDS     = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.is_active and not self.activation_date:
            self.activation_date = timezone.now()
        super().save(*args, **kwargs)


@receiver(post_save, sender=CustomUser)
def delete_inactive_user(sender, instance, created, **kwargs):
    if not created and not instance.is_active:
        if instance.activation_date and timezone.now() - instance.activation_date > timezone.timedelta(hours=1):
            instance.delete()


