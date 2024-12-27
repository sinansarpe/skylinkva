from django.contrib import admin

from .models import EventType, Events, SKYLinkEvents

# Register your models here.


class EventTypeAdmin (admin.ModelAdmin):
    pass

admin.site.register(EventType, EventTypeAdmin)

class EventsAdmin (admin.ModelAdmin):
    pass

admin.site.register(Events, EventsAdmin)




class SkylinkEventsAdmin (admin.ModelAdmin):
    pass

admin.site.register (SKYLinkEvents, SkylinkEventsAdmin)