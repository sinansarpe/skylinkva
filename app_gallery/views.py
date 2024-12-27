from django.shortcuts import render

from app_airline.models import Airline, Partnerships
from app_community.models import Screenshots

# Create your views here.

def gallery (request):

    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)
    screenshots         = Screenshots.objects.filter(is_published=True).order_by('-uploaded_at')


    context             = {
                            'airline':airline,
                            'partners':partners,
                            'screenshots':screenshots,

                        }
    template            = 'gallery.html'
    return render(request, template, context)