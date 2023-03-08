from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from pyexpat.errors import messages
from .helpers import send_forget_password_mail
from api.authentication.models import RegisterFreelancer


# Create your views here.
@require_http_methods(["POST"])
def emailResetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not RegisterFreelancer.objects.filter(email=email).first():
            messages.success(request,'no email matchs ',email)
            return redirect ('/forgetPassword')
        email_obj= RegisterFreelancer.get(email=email)
        send_forget_password_mail(email_obj , token)