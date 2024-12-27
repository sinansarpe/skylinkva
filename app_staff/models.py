import os
from django.db import models
from django.core.exceptions import ValidationError

from app_airline.models import Fleet

# Create your models here.

class UploadLivery (models.Model):

    order           = models.SmallIntegerField          ('Order', default=1)
    designator      = models.ForeignKey                 (Fleet, on_delete=models.CASCADE, verbose_name='Designator', null=True, blank=True)
    title           = models.CharField                  ('Title', max_length=100)
    livery          = models.FileField                  ('Livery File', upload_to='uploads/airline/livery')
    description     = models.TextField                  ('Description', help_text='Additional information if required', null=True, blank=True)
    upload_date     = models.DateField                  ('Uploaded at', auto_now_add=True)
    livery_image    = models.ImageField                 ('Livery Image', upload_to='uploads/airline/livery/image', null=True, blank=True)

    class Meta:
        verbose_name ="Aircraft Livery Upload"
        verbose_name_plural ="Aircraft Livery Uploads"

    
    def clean(self):
        super().clean()
        # Validate file extension
        if self.livery:
            valid_extensions = ['.zip', '.rar']
            if not any(self.livery.name.endswith(ext) for ext in valid_extensions):
                raise ValidationError({'livery': "Only ZIP or RAR files are allowed."})


    def delete(self, *args, **kwargs):
        # Delete associated files
        if self.livery:
            if os.path.isfile(self.livery.path):
                os.remove(self.livery.path)
        if self.livery_image:
            if os.path.isfile(self.livery_image.path):
                os.remove(self.livery_image.path)
        # Call the parent class's delete method
        super().delete(*args, **kwargs)


    def __str__ (self):
        return self.title


