import requests
from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from app_users.models import CustomUser

from .models import (
                        Airline, Partnerships,
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
                        Faq, FaqCategories,
                    )

# from app_database.models import StaffPositions, Faq
# Create your views here.

def Staffs (request):
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)

    staffs      = CustomUser.objects.all().filter(is_active=True, is_pilot=True, is_vastaff=True)
    #staffpos    = StaffPositions.objects.all().filter(staff_pos_isFilled=False)


    context     = {
                    'airline':airline,
                    'partners':partners,
                    'staff':staffs,
                    #'staffpos':staffpos,

                  }
    template    = 'staff.html'

    return render(request, template, context)

def Roster (request):

    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)
    ivao        = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True, partner_shortName__startswith="IVAO",  )
    
    roster      = CustomUser.objects.all().filter(is_active=True, is_pilot=True)

    context     = {
                    'airline':airline,
                    'partners':partners,
                    'ivao':ivao,
                    'roster':roster,

                }
    template    = 'roster.html'
    return render(request, template, context)


def resources (request):
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)
    #faq         = Faq.objects.all()

    context     = {
                    'airline':airline,
                    'partners':partners,
                    #'faq':faq

                }
    template    = 'resources.html'
    return render(request, template, context)


def activeFlights (request):

    context     = {


                }
    template    = 'activeFlights.html'
    return render(request, template, context)



def rules (request):
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)

    rules       = RulesRegulations.objects.all().order_by('rules_order')
    rulesupdates= RulesRegulationsUpdate.objects.all()


    context             = {
                                'airline':airline,
                                'partners':partners,
                                'rules':rules,
                                'rulesupdates':rulesupdates,

                        }
    template            = 'rules.html'
    return render(request, template, context)


def ranking (request):

    airline         = Airline.objects.all().first()
    partners        = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)

    ranking         = RankingSystem.objects.all().order_by('ranking_order')
    rankingupdates  = RankingSystemUpdate.objects.all()
    ranks           = AirlineBadges.objects.all()

    context             = {
                                'airline':airline,
                                'partners':partners,
                                'ranking':ranking,
                                'ranks':ranks,
                                'rankingupdates':rankingupdates,

                        }
    template            = 'ranking.html'
    return render(request, template, context)


def flightops (request):

    airline         = Airline.objects.all().first()
    partners        = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)

    basehubs        = BaseHubs.objects.all().order_by('order')
    aircrafts       = Aircraft.objects.all().filter(is_active=True).order_by('designator', 'registration')
    s_flights       = ScheduledFlights.objects.all().filter(is_active=True)

    context             = {
                                'airline':airline,
                                'partners':partners,
                                'basehubs':basehubs,
                                'aircrafts':aircrafts,
                                's_flights':s_flights,


                        }
    template            = 'flightops.html'
    return render(request, template, context)



def privacy (request):

    airline         = Airline.objects.all().first()
    partners        = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)

    privacy         = PrivacyPolicy.objects.all()


    context         = {

                        'airline':airline,
                        'partners':partners,
                        'privacy':privacy,

                    }
    template        = 'privacy-policy.html'
    return render(request, template, context)    


def faq (request):

    airline         = Airline.objects.all().first()
    partners        = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)

    faq             = Faq.objects.all()


    context         = {

                        'airline':airline,
                        'partners':partners,
                        'faq':faq,

                    }
    template        = 'faq.html'
    return render(request, template, context)    