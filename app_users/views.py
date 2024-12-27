import requests
from . import forms 
from django.shortcuts import render, redirect,get_object_or_404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout 

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from .forms import SignupForm
# PASSWORD RESET
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth import get_user_model
from .models import CustomUser #, UserImageContent, UserTextContent
User = get_user_model()

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import redirect

from app_airline.models import Airline, Partnerships
#from airline_db.models import StaffPositions

from django.views.generic import View

from django.http import JsonResponse
#from .forms import ScreenshotUploadForm, UserContentForm

from .validators import validate_screenshot
from PIL import Image

from django.core.exceptions import PermissionDenied

from app_community.models import Screenshots

# Create your views here.

def signin(request):
    success_url = reverse_lazy('dashboard')  # Replace 'dashboard' with your desired URL name
    
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.all()
    template = loader.get_template('login.html')
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                
                return redirect('dashboard')
            else:
                message = 'Girdiğiniz bilgiler eksik veya hatalı, lütfen tekrar deneyiniz.'
    return render(
        request, 'login.html', context={'form': form, 'message': message, 'airline':airline,'partners':partners,})

    def get_success_url(self):
        return self.success_url


def signout(request):
    auth_logout(request)
    return redirect('/')


def signup(request): # https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
    
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.all()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'SKYLink E-mail Verification'
            message = render_to_string('acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #return HttpResponse('Dogrula!')
            return render(request, 'activation-sent.html',{'airline':airline,'partners':partners,})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form, 'airline':airline,'partners':partners})

def activate(request, uidb64, token):

    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.all()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        #uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'activation_success.html',{'airline':airline,'partners':partners,})
    else:
        return render(request, 'activation_invalid.html',{'airline':airline,'partners':partners,})


def password_reset_success(request):
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.all()

    return render(request, 'password_reset_success.html',{'airline':airline,'partners':partners,})

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.all()

    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."

    success_url = reverse_lazy('password_reset_success')

    def get_context_data(self, **kwargs):
            # Call the base implementation to get the existing context
            context = super().get_context_data(**kwargs)

            # Add custom context
            context['airline'] = Airline.objects.all().first()
            context['partners'] = Partnerships.objects.all()

            return context
# =========================
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def get_context_data(self, **kwargs):
        # Get the default context
        context = super().get_context_data(**kwargs)

        # Add custom context
        context['airline'] = Airline.objects.all().first()
        context['partners'] = Partnerships.objects.all()

        return context
    
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the existing context
        context = super().get_context_data(**kwargs)

        # Add custom context
        context['airline'] = Airline.objects.all().first()
        context['partners'] = Partnerships.objects.all()

        return context


def password_reset_airline (request):
    airline     = Airline.objects.all().first()
    partners    = Partnerships.objects.all()

    return render(request, 'password_reset_html',{'airline':airline,'partners':partners,})


