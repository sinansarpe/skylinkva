from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from app_users.models import CustomUser
from app_airline.models import Airline, Partnerships, AirlineBadges
from app_community.models import Screenshots

from .forms import UploadLiveryForm
from .models import UploadLivery

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


#from .forms import vamsysIDForm

# Create your views here.

# ================================================================
# Approve Screenshots 


def office_page (request):

    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)   
    approving_ss_count  = Screenshots.objects.filter(is_published=False).count()
    applicants_count    = CustomUser.objects.filter(is_active=True, apply_for_pilot=True).count()    

    context             = {
                            'airline':airline,
                            'partners':partners,
                            'applicants_count':applicants_count,
                            'approving_ss_count':approving_ss_count,
                           }
    template            = 'office.html'
    return render(request, template, context)  


def approve_screenshots(request):

    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)
    applicants_count    = CustomUser.objects.filter(is_active=True, apply_for_pilot=True).count()   

    approving_ss_count  = Screenshots.objects.filter(is_published=False).count()
    approving_ss        = Screenshots.objects.filter(is_published=False)

    context             = {
                            'airline':airline,
                            'partners':partners,
                            'applicants_count':applicants_count,

                            'approving_ss':approving_ss,
                            'approving_ss_count':approving_ss_count,
                           }
    template            = 'approve_ss.html'
    return render(request, template, context)

def ss_approved (request, id):

    ss_approved = Screenshots.objects.filter(is_published=False, id=id).update (is_published=True) 
  
    return redirect ('approve_screenshots')


# ================================================================
# Approve Applicants 

def applicants (request):

    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)
    approving_ss_count  = Screenshots.objects.filter(is_published=False).count()    
    
    
    applicants          = CustomUser.objects.filter(is_active=True, apply_for_pilot=True, is_invitation_sent=False)
    applicants_invited  = CustomUser.objects.filter(is_active=True, apply_for_pilot=True, is_invitation_sent=True)
    applicants_count    = CustomUser.objects.filter(is_active=True, apply_for_pilot=True).count()

 # ===========================================
# 
    if request.method == "POST":
        print("Form data:", request.POST)  # Debug: Check submitted form data

        # Loop through all the submitted form data
        user_id = request.POST.get("user_id")
        vamsys_id = request.POST.get("vamsys_id")
        first_title = AirlineBadges.objects.get(id=1)
        print(f"Received user_id: {user_id}, vamsys_id: {vamsys_id}")

        if user_id and vamsys_id:
            try:
                # Fetch the specific user to update
                user = CustomUser.objects.get(id=user_id, is_active=True, apply_for_pilot=True, is_invitation_sent=True)

                # Update the user's fields
                user.vamsys_id = vamsys_id
                user.is_pilot = True
                user.apply_for_pilot = False
                user.is_onTrial=True
                user.pilot_title=first_title
                user.save()  # Save changes to the database

                print(f"User {user.id} updated: vamsys_id={user.vamsys_id}, is_pilot={user.is_pilot}")
            except CustomUser.DoesNotExist:
                print(f"User with id {user_id} not found or not eligible for update.")
            except Exception as e:
                print(f"Error updating user {user_id}: {e}")

        else:
            print("user_id or vamsys_id is missing.")

        return redirect('applicants')  # Redirect after processing
 
    # For GET request, render the table
    users = CustomUser.objects.filter(is_active=True, apply_for_pilot=True, is_invitation_sent=True)[:1]                          


# ===========================================    

    context             = {
                            'airline':airline,
                            'partners':partners,
                            'approving_ss_count': approving_ss_count,


                            'applicants':applicants,
                            'applicants_count':applicants_count,
                            'applicants_invited':applicants_invited,
                            'users':users,




                           }
    template            = 'approve_applicant.html'
    #return redirect('applicants')
    return render(request, template, context)  


def invited (request, id):

    invited = CustomUser.objects.filter(is_active=True, apply_for_pilot=True, is_invitation_sent=False, id=id).update(is_invitation_sent=True)

    return redirect('applicants')


# ================================================================
# UPLOAD LIVERY

def upload_livery_view(request):

    airline             = Airline.objects.all().first()
    partners            = Partnerships.objects.all().filter(airline_shortName=airline, partner_active=True)
    liveries            = UploadLivery.objects.all()
    approving_ss_count  = Screenshots.objects.filter(is_published=False).count()
    applicants_count    = CustomUser.objects.filter(is_active=True, apply_for_pilot=True).count() 

    """Handle the upload of livery files."""
    if request.method == "POST":
        form = UploadLiveryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Saves the data and uploaded file to the database
            return redirect('upload_livery')  # Replace 'success' with the URL or name of your success page
    else:
        form = UploadLiveryForm()
    return render(request, 'upload_livery.html', {'form': form,
                                                  'airline':airline, 
                                                  'partners':partners,
                                                  'applicants_count':applicants_count,
                                                  'approving_ss_count':approving_ss_count,
                                                  'liveries':liveries,
                                               
                                                  })



class LiveryDeleteView(DeleteView):
    model = UploadLivery
    template_name = 'livery_confirm_delete.html'
    success_url = reverse_lazy('upload_livery')  # Redirect to the list view after deletion

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)

        # Add custom context
        context['airline'] = Airline.objects.all().first()
        context['partners'] = Partnerships.objects.all()
        context['approving_ss_count']  = Screenshots.objects.filter(is_published=False).count()
        context['applicants_count']    = CustomUser.objects.filter(is_active=True, apply_for_pilot=True).count() 

        return context