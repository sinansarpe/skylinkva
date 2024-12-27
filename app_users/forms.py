from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import (CustomUser, 
                     #UserImageContent,UserTextContent 
                     )

from .validators import validate_screenshot
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
User = get_user_model()


class SignupForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text='')
    class Meta:
        model = CustomUser
        fields = ('apply_for_pilot','email', 'username', 'password1', 'password2', 'ivao_id', 'first_name', 'last_name','age',)
        labels = {
                    "username": "Username:",
                    "email": "E-mail:",
                    "password1": "Password:",
                    "password2": "Password Again:",
                    "apply_for_pilot":"I want to be your pilot.",
                    "ivao_id": "IVAO ID (VID):",
                    "first_name":"First Name:",
                    "last_name":"Last Name:",
                    "age":"Date of Birth",


                }
        

    def clean_age(self):
        dob = self.cleaned_data.get("age")
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                raise ValidationError("You must be at least 18 years old to register.")
        return dob


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v


    '''
    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("User with this email address already exists.")
       return self.cleaned_data
    '''

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        labels = {
                    "email": "E-mail:",
                    "password": "Password:",

                }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v


'''
class ScreenshotUploadForm(forms.ModelForm):
    class Meta:
        model = UserImageContent
        fields = ('image_title','image_content')
        labels = {
                    "image_title": "How do you name this Screenshot:",
                    "image_content": "Image:",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v
    
    

    def clean_screenshot(self):
        screenshot = self.cleaned_data.get('image_content')
        if screenshot:
            validate_screenshot(screenshot)  # Reuse the validation function
        return screenshot


class UserContentForm(forms.ModelForm):
    class Meta:
        model   = UserTextContent 
        fields  = ('text_title', 'text_content')
        text_content =  SummernoteTextField()
        labels  = {
                    "text_title":"Your Title",
                    "text_content":""
                   }
        widgets = {
            'text_content': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v        
'''