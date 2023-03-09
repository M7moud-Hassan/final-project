from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from django.contrib.auth.hashers import make_password ,check_password
from django.core.mail import EmailMessage
from .models import RegisterFreelancer
from .serlializers import SignUpFreelancerSerializer
from .tokens import account_activation_token
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from .token import email_verification_token
from rest_framework.decorators import api_view


@api_view(['GET'])
def verfy_email(request,token,uid):
    uid = force_str(uid)
    user = RegisterFreelancer.objects.filter(id=uid)
    if user is not None and email_verification_token.check_token(user, token):
        user.is_activate=True
        return Response(user)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def signup_freeLancer(request):
    user = SignUpFreelancerSerializer(data=request.data)
    if user.is_valid():
        hashedpassword = make_password(user.data['password'])
        register=RegisterFreelancer.objects.create(first_name=user.data['first_name'],
                                         last_name=user.data['last_name'],email=user.data['email'],
                                         password=hashedpassword,phone_number=user.data['phone_number'],
                                          is_active=False)

        current_site = get_current_site(request)
        mail_subject = 'Activation link has been sent to your email id'
        messages ={
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(register.id)),
            'token': account_activation_token.make_token(register),
        }

        to_email = [user.data['email']]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, 'message', from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

