from django import forms
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model

from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django.core.exceptions import ValidationError
from .models import UploadLivery
from app_users.models import CustomUser



class UploadLiveryForm(forms.ModelForm):
    class Meta:
        model = UploadLivery
        fields = ['title', 'livery', 'livery_image', 'description',]

    def clean_livery(self):
        livery = self.cleaned_data.get('livery')
        if livery:
            valid_extensions = ['.zip', '.rar']
            if not any(livery.name.lower().endswith(ext) for ext in valid_extensions):
                raise ValidationError("Only ZIP or RAR files are allowed.")
        return livery
