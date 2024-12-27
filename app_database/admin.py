from django.contrib import admin

from .models import (
                        Networks,
                        PilotBadges, ATCBadges,
                        Divisions
                    )
# Register your models here.

class DivisionsInline (admin.TabularInline):
    model       = Divisions
    extra       = 0

class PilotBadgesInline (admin.TabularInline):
    model       = PilotBadges
    extra       = 0

class ATCBadgesInline (admin.TabularInline):
    model       = ATCBadges
    extra       = 0

class NetworksAdmin (admin.ModelAdmin):

    inlines     = [
                    DivisionsInline,
                    PilotBadgesInline, 
                    ATCBadgesInline,
                ]

    pass

admin.site.register (Networks, NetworksAdmin)


