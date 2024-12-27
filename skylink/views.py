from django.shortcuts import render, get_object_or_404
import requests
import json
from django.http import JsonResponse
from django.db.models import Q


from django.contrib.auth.decorators import login_required

from app_airline.models import Airline, Partnerships, Offers, AirlineLandingImage, News #, AirlineFlightsJson #,Social, Awards,
from app_events.models import EventType, Events, SKYLinkEvents

from .forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings


client_id  = '5b8f4604-cffd-4054-9110-1989fc4a999a'
client_secret = 'B6a3OMab47sIQRrwdzRi5mGtJ73d3Rum'


def airline (request):

    airline = Airline.objects.all().first()
    return {'airline':airline}

def partners (request):
    
    partners= Partnerships.objects.filter(airline_shortName=airline, partner_active=True)
    return {'partners':partners}

def landing (request,*args, **kwargs):
    
    #IVAO JSON
    url = "https://api.ivao.aero/v2/tracker/whazzup"
    response = requests.get(url)
    data = response.json()
    
    voice = data['voiceServers']
    clients = data['clients']

    #vaMSYS JSON
    url = "https://vamsys.io/statistics/1b6a7b10-1ece-4c4f-b5b9-bb44db5cd77e"
    vresponse = requests.get(url)
    vamsysdata = vresponse.json()
    latestPirep = vamsysdata['latestPirep']
    pilots      = vamsysdata['pilots']
    transport   = vamsysdata['transport']
    pireps      = vamsysdata['pireps']
    flightTime = vamsysdata['flightTime']



    airline         = Airline.objects.all().first()
    landingImage    = AirlineLandingImage.objects.filter(is_Published=True).last()
    partners        = Partnerships.objects.filter(airline_shortName=airline, partner_active=True)
    news            = News.objects.filter(is_published=True).order_by('-id')[:1]    
    hqevents        = Events.objects.all().first()
    skylinkevents   = SKYLinkEvents.objects.all()
    #hqevents        = HQEvents.objects.all().first()
    #trevents        = TREvents.objects.all().last()
    #social         = Social.objects.filter(airline_shortName=airline, social_active=True)
    #awards         = Awards.objects.filter(airline_shortName=airline)
    offers          = Offers.objects.filter(airline_shortName=airline, offer_published=True).order_by('offer_order')

    
    context     = {
                        'airline':airline,
                        'partners':partners,
                        'offers':offers,
                        'news':news,
                        'hqevents':hqevents,

                        'skylinkevents':skylinkevents,

                        'landingImage':landingImage,
                        #'social':social,
                        #'awards':awards,
                        'voice':voice,
                        'clients':clients,
                        

                        'latestPirep':latestPirep,
                        'pilots':pilots,
                        'transport': transport,
                        'pireps':pireps,
                        'flightTime':flightTime,

 
                   }

    template        = 'landing.html'
    return render(request, template, context)

#@login_required
def index (request):
    
    #airline         = Airline.objects.all().first()
    partners        = Partnerships.objects.all().filter(irline_shortName=airline, partner_active=True)    
    
    context         = {
                        'airline': airline,
                        'partner': partners,
                       }
    template        = 'index.html'
    return render(request, template, context)


def vamsys_pilot(request):

    pilot = request.user.vamsys_id

# API details
    api_url = "https://vamsys.io/api/token/v1/airline/pilot"
    api_token = "319|cFqOHPQOrBhs3ALtv5g2u4WORd5jnCtqeLDFr26Vdf0c5f02"


    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    # Add the required field (adjust based on API documentation)
    #payload = {"username": "pilot"}
    payload = {"username": pilot}
    try:
        # Use POST if the API requires a body; adjust to GET or another method if needed
        response = requests.post(api_url, headers=headers, json=payload)

        # Log response for debugging
        print(pilot)
        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Body:", response.text)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            # Return API error message for better debugging
            return JsonResponse({
                "error": f"Failed to fetch data, status code: {response.status_code}",
                "raw_response": response.text,
            }, status=response.status_code)

    except requests.RequestException as e:
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
    



def airport(request):

    pilot = request.user.vamsys_id

# API details
    api_url = "https://vamsys.io/api/token/v1/discord/airport/find"
    api_token = "318|61tMS1N5o1yblU1J11IvRVxvY0vESGZ4lS7URq9fdeb0fad7"


    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }

    # Add the required field (adjust based on API documentation)
    #payload = {"username": "pilot"}
    payload = {"airport_code": "LTFE"}
    try:
        # Use POST if the API requires a body; adjust to GET or another method if needed
        response = requests.post(api_url, headers=headers, json=payload)

        # Log response for debugging
        print(pilot)
        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Body:", response.text)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            # Return API error message for better debugging
            return JsonResponse({
                "error": f"Failed to fetch data, status code: {response.status_code}",
                "raw_response": response.text,
            }, status=response.status_code)

    except requests.RequestException as e:
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)


class ContactFormView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')  # Redirect to the same page after submission

    def form_valid(self, form):
        # Process the form data (e.g., send an email)
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # Construct the email content
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        send_mail(subject, full_message, settings.DEFAULT_CONTACT_EMAIL, [settings.DEFAULT_CONTACT_EMAIL])

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            # Call the base implementation to get the existing context
            context = super().get_context_data(**kwargs)

            # Add custom context
            context['airline'] = Airline.objects.all().first()
            context['partners'] = Partnerships.objects.all()

            return context










#IVAO API
#client_id       ="d785a3f2-020d-48b7-8ebc-ddc371352988"
#client_secret   ="7tRtkEKRxaaUyPIYoKeN62aEeTpi6bY2"
