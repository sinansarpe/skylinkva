from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.core.exceptions import PermissionDenied

from app_users.models import CustomUser
from app_airline.models import Airline, Partnerships
from app_staff.models import UploadLivery
from .models import Screenshots
from .forms import ScreenshotForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


# Create your views here.

# =========================================================================
# DASHBOARD MAIN

@login_required
def dashboard (request):

    pilot_applicants    = CustomUser.objects.all().filter(is_active=True, apply_for_pilot=True)
    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)  

    profile             = CustomUser.objects.all().filter(is_active=True, username = request.user.username)

    dashboard_ss        = Screenshots.objects.filter(username=request.user, is_published=True)
    ss_hold_approval    = Screenshots.objects.all().filter(username=request.user, is_published=False)

    applicants_count    = CustomUser.objects.filter(is_active=True,apply_for_pilot=True).count()
    applicants          = CustomUser.objects.filter(is_active=True,apply_for_pilot=True)

    approving_ss_count  = Screenshots.objects.filter(is_published=False).count()

    

    user = request.user.username
    current_user = request.user
    username = current_user.username




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
    response = requests.post(api_url, headers=headers, json=payload)
    data = response.json()
    
    '''
    try:
        # Use POST if the API requires a body; adjust to GET or another method if needed
        response = requests.post(api_url, headers=headers, json=payload)

        # Log response for debugging
        #print(pilot)
        #print("Status Code:", response.status_code)
        #print("Response Headers:", response.headers)
        #print("Response Body:", response.text)

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
    '''

    context     = {
                        'airline':airline,
                        'partners':partners,
                        'profile':profile,
                        'cuser':current_user,
                        'user_imgs':dashboard_ss,
                        'ss_waiting_approval':ss_hold_approval,
                        'response':response,
                        'data':data,

                        'applicants_count':applicants_count,
                        'applicants':applicants,

                        'approving_ss_count':approving_ss_count,

                        # USER MANAGEMENT by STAFF
                        'pilot_applicant':pilot_applicants,

        }

    template    = 'dashboard.html'
    return render(request, template, context)


# =========================================================================
# UPLOAD - SCREENSHOT FORM

def screenshots_form (request):
    user                = request.user
    #username            = request.user.username 

    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)  
    username            = CustomUser.objects.filter(is_active=True)
    ss_user             = Screenshots.objects.filter(is_published=True, username=user).order_by('-uploaded_at')
    ss_waiting_approval = Screenshots.objects.filter(is_published=False, username=user).count()
    ss_waiting          = Screenshots.objects.filter(is_published=False, username=user)

    approving_ss_count  = Screenshots.objects.filter(is_published=False).count()

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
    response = requests.post(api_url, headers=headers, json=payload)
    data = response.json()    

    current_user = request.user
    username = current_user.username

    if request.method == 'POST':
        ssform = ScreenshotForm(request.POST, request.FILES)
        if ssform.is_valid():
            # Check if the user has reached the 12-screenshot limit
            if request.user.screenshots.count() >= 12:
                messages.error(request, 'You can only upload a maximum of 12 screenshots. To upload more, you need to delete existing one(s).')
                #return render(request, 'screenshots_form.html',{'ssform': ssform})
                return redirect('screenshots_form')

            ssform.instance.username = request.user
            ssform.save()
            messages.success(request, 'Screenshot uploaded successfully.')
            #return render(request, 'screenshots_form.html', {'ssform': ssform})
            return redirect('screenshots_form')
           
    else:
        ssform = ScreenshotForm()


    context     = {
                        'airline':airline,
                        'partners':partners,
                        'data':data,                        
                        'ssform': ssform,
                        'cuser':current_user,

                        'ss_waiting_approval':ss_waiting_approval,
                        'ss_waiting':ss_waiting,
                        'approving_ss_count':approving_ss_count,
                        'ss_user':ss_user,
    }

    template    = 'screenshots_form.html'
    return render(request, template, context)

def delete_image(request, id):
    image = Screenshots.objects.get(id=id)

    if request.user != image.username:
        raise PermissionDenied("You don't have permission to delete this image.")
    
    image.delete()
    return redirect('screenshots_form')  # Redirect to a list view

def delete_published(request,id):
    
    image = Screenshots.objects.get(id=id)
    
    if request.user != image.username:
        raise PermissionDenied("You don't have permission to delete this image.")
    
    image.delete()
    return redirect('screenshots_form') 


# =========================================================================
# DOWNLOAD LIVERY

def downloadLivery (request):

    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)      

    liveries            = UploadLivery.objects.all().order_by('title')

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
    response = requests.post(api_url, headers=headers, json=payload)
    data = response.json()



    context         = {
                        'airline':airline,
                        'partners':partners,
                        'data':data,
                        'liveries':liveries,

                    }    
    template        = 'download-livery.html'
    return render(request, template, context)


# =========================================================================
# STAFF JOB - HIRE PILOT
@login_required
def pilot_application(request):
    user = request.user
    user.apply_for_pilot = True
    user.save()
    return redirect('dashboard')  # Redirect to a desired view

@login_required
def pilot_hired(request, id):

    applicant = CustomUser.objects.filter(is_active=True, apply_for_pilot = True, id=id).update(
                                                                                            is_pilot = True,
                                                                                            is_onTrial = True,
                                                                                            apply_for_pilot = False,
                                                                                            pilot_title = "1",
                                                                                            )
    return redirect('dashboard')  # Redirect to a desired view


@login_required
def delete_account (request):

    return render(request, 'confirm_account_deletion.html')

class DeleteAccountView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Delete the user's account
        user = request.user
        user.delete()
        return redirect('landing')  # Redirect to a confirmation page or home