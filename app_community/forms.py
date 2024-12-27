from django import forms
from django.contrib.auth import get_user_model

from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from app_users.models import (CustomUser, )
from .models import Screenshots


User = get_user_model()

class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshots
        fields = ['image']

        labels = {

                    "image": "Screenshot",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v

