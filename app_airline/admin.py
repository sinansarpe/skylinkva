from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

from .models import (
                        Airline, AirlineLandingImage,
                        Partnerships,
                        AirlineBadges,
                        StaffPositions, StaffPositionRevisions, 
                        Offers,News,
                        BaseHubs, Scenery,
                        Fleet, Aircraft,
                        RulesRegulations, RulesRegulationsUpdate,
                        FlightOperations, FlightOperationsUpdate,
                        RankingSystem, RankingSystemUpdate,
                        Downloads,
                        ScheduledFlights,
                        PrivacyPolicy,
                        FaqCategories,Faq,

                    )

# Register your models here.

class AirlineLandingImageInline (admin.TabularInline):

    model           = AirlineLandingImage
    extra           = 0

class PartnershipsInline (admin.StackedInline):
    model           = Partnerships
    extra           = 0

class OffersInline (admin.StackedInline):
    model           = Offers
    extra           = 0

class AirlineAdmin (SummernoteModelAdmin):
    summernote_fields   = '__all__'
    inlines         = [
                        AirlineLandingImageInline,
                        OffersInline,
                        PartnershipsInline,

                    ]
    pass

admin.site.register(Airline, AirlineAdmin)


class AirlineBadgesAdmin (admin.ModelAdmin):
    
    list_display    = [
                        'pilot_title',
                        'badge_order',
                        'req_hours',
                        'req_pireps',
                        'req_points',
                        'req_bonus_points',
                        'req_atc_badge',
                        'req_pilot_badge'
                    ]
    
    ordering        = ['badge_order',]

admin.site.register (AirlineBadges, AirlineBadgesAdmin)


class StaffPositionRevisionsInline (admin.StackedInline):
    
    model           = StaffPositionRevisions
    extra           = 0

class StaffPositionsAdmin (admin.ModelAdmin):

    inlines         = [StaffPositionRevisionsInline]

    list_display    = [
                            'staff_title',
                            'staff_order',
                            'staff_title_abbr',
                            'staff_pos_email',
                            'staff_pos_hiring',
                    ]
    ordering        = ['staff_order',]

admin.site.register (StaffPositions, StaffPositionsAdmin)

class NewsAdmin (admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)


class SceneryInline (admin.StackedInline):
    
    model           = Scenery
    extra           = 0

class BaseHubsAdmin (admin.ModelAdmin):
    
    inlines         = [SceneryInline]

admin.site.register(BaseHubs, BaseHubsAdmin)


class AircraftInline (admin.StackedInline):

    model           = Aircraft
    extra           = 0

class FleetAdmin (admin.ModelAdmin):

    inlines         = [AircraftInline]

admin.site.register(Fleet, FleetAdmin)


class RulesRegulationsInline (admin.StackedInline):
    model               = RulesRegulationsUpdate
    extra               = 0

class RulesRegulationsAdmin (SummernoteModelAdmin):
    summernote_fields   = '__all__'
    inlines             = [RulesRegulationsInline,]

admin.site.register (RulesRegulations, RulesRegulationsAdmin)

class FlightOperationsUpdateInline (admin.StackedInline):
    model               = FlightOperationsUpdate
    extra               =  0

class FlightOperationsAdmin (SummernoteModelAdmin):
    summernote_fields   = '__all__'
    inlines             = [FlightOperationsUpdateInline,]

admin.site.register(FlightOperations, FlightOperationsAdmin)

class RankingSystemUpdateInline (admin.StackedInline):
    model               = RankingSystemUpdate
    extra               =  0

class RankingSystemAdmin (SummernoteModelAdmin):
    summernote_fields   = '__all__'
    inlines             = [RankingSystemUpdateInline]

admin.site.register(RankingSystem, RankingSystemAdmin)

class ScheduledFlightsAdmin (admin.ModelAdmin):
    pass

admin.site.register(ScheduledFlights, ScheduledFlightsAdmin)


class PrivacyPolicyAdmin (SummernoteModelAdmin):
    summernote_fields   = '__all__'
    pass

admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)


class FaqInline (admin.StackedInline):

    model               = Faq
    extra               = 0

class FaqCategoriesAdmin (admin.ModelAdmin):
    
    inlines             = [FaqInline,]

admin.site.register(FaqCategories, FaqCategoriesAdmin)