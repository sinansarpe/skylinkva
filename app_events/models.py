from django.db import models

# Create your models here.

class EventType (models.Model):
    
    type                = models.CharField              ('Event Type', max_length=30)
    type_image          = models.ImageField             ('Event Owner Image', upload_to='uploads/airline/events/types', null=True, blank=True)


    class Meta:
        verbose_name ="Event Type"
        verbose_name_plural ="Event Types"

    def __str__ (self):
        return self.type

class Events (models.Model):

    type                = models.ForeignKey             (EventType, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Event Type')
    title               = models.CharField              ('Title', max_length=100)
    event_image         = models.ImageField             ('Event Image', upload_to='uploads/airline/events', null=True, blank=True)
    description         = models.TextField              ('Description', null=True, blank=True)
    event_url           = models.URLField               ('Link', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name ="HQ Event"
        verbose_name_plural ="HQ Events"

    def __str__ (self):
        return self.title




class SKYLinkEvents (models.Model):

    title               = models.CharField              ('Title', max_length=100)
    image               = models.ImageField             ('Event Image', upload_to='uploads/airline/events/SKYLINK', null=True, blank=True)
    description         = models.TextField              ('Description', null=True, blank=True)
    event_url           = models.URLField               ('Link', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name ="Skylink Event"
        verbose_name_plural ="Skylink Events"

    def __str__ (self):
        return self.title