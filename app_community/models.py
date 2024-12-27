from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image

from app_airline.models import BaseHubs, Fleet

from app_users.models import CustomUser

# Create your models here.

def validate_aspect_ratio_16_9(image):
    """
    Validate that the uploaded image has a 16:9 aspect ratio.
    """
    with Image.open(image) as img:
        width, height = img.size
        if round(width / height, 2) != round(16 / 9, 2):  # Allow for slight floating-point differences
            raise ValidationError("The image must have a 16:9 aspect ratio.")

class Screenshots(models.Model):
    #user = models.CharField('user')
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='screenshots', null=True, blank=True)
    image = models.ImageField('Screenshot', upload_to='members/uploads/screenshots/images', null=True, blank=True,validators=[validate_aspect_ratio_16_9])
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_published = models.BooleanField ('is Published', default=False)
    is_featured = models.BooleanField ('is Featured', default=False)
    is_mainpage = models.BooleanField ('Published in Main', default=False)

    def __str__(self):
        return f"Screenshot by {self.username}"
    


