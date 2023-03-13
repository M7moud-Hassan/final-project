import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from pyexpat.errors import messages
from .helpers import send_forget_password_mail
from .models import RegisterFreelancer, RegisterUser, Experience, Services, Skills
from django.contrib.auth.hashers import make_password

# Create your views here.

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from django.contrib.auth.hashers import make_password ,check_password
from django.core.mail import EmailMessage

from .models import RegisterFreelancer
from .serlializers import SignUpFreelancerSerializer , SignUpUserSerialzer
from .tokens import account_activation_token , Reg_Token
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def signup_freeLancer(request):
    user = SignUpFreelancerSerializer(data=request.data)
    if user.is_valid():
        hashedpassword = make_password(user.data['password'])
        register=RegisterFreelancer.objects.create(first_name=user.data['first_name'],
                                         last_name=user.data['last_name'],email=user.data['email'],
                                         password=hashedpassword,phone_number=user.data['phone_number'],
                                          is_active=False,job_title=None,overview=None,hourly_rate=None,
                                                   user_image=None,street_address=None,city=None,
                                                   state=None,postal_code=None)

        mail_subject = 'Activation link has been sent to your email id'
        messages ="http://current_site.domain/activate?uid="+str(urlsafe_base64_encode(force_bytes(register.id)))+"&token="+account_activation_token.make_token(register)

        to_email = [user.data['email']]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, messages, from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def registerUserSerialzer(request):
    user = SignUpUserSerialzer(data=request.data)
    if user.is_valid():
        hashPassword = make_password(user.data['password'])
        input=RegisterUser.objects.create(fname=user.data['fname'],lname=user.data['lname'],email=user.data['email'],
        password=hashPassword,phone=user.data['phone'])

        mail_subject = 'Activation link has been sent to your email id'
        messages = "http://current_site.domain/activate?uid=" + str(
            urlsafe_base64_encode(force_bytes(input.id))) + "&token=" + Reg_Token.make_token(input)

        to_email = [user.data['email']]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, messages, from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def verify_user_email(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterUser.objects.filter(id=uid).first()
    if user is not None and Reg_Token.check_token(user, request.data['token']):
        user.is_active=True
        user.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def verfy_email(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterFreelancer.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):
        user.is_active=True
        user.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def emailResetPassword(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required.'}, status=400)

    user = RegisterFreelancer.objects.filter(email=email).first()
    if not user :
        return Response({'error': 'User not found.'}, status=404)
    # if not user.is_active:
    #     return Response({'error': 'User not activate.'}, status=404)

    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_url = f'http://auth/rest_password/{uid}/{token}/'

    send_mail(
        'Password Reset',
        f'Click the following link to reset your password: {reset_url}',
        'soonfu0@gmail.com',
        [email],
        fail_silently=False,
    )

    return Response({'message': 'Password reset email sent.'}, status=200)
@api_view(['POST'])
def resetPasswordView(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterFreelancer.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):

        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def email_rest_password_user(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required.'}, status=400)

    user = RegisterUser.objects.filter(email=email).first()
    if not user :
        return Response({'error': 'User not found.'}, status=404)

    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_url = f'http://auth/rest_password_user/{uid}/{token}/'

    send_mail(
        'Password Reset',
        f'Click the following link to reset your password: {reset_url}',
        'soonfu0@gmail.com',
        [email],
        fail_silently=False,
    )

    return Response({'message': 'Password reset email sent.'}, status=200)


@api_view(['POST'])
def rest_password_view_user(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterUser.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):

        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addExperinece (request):

    data = json.loads(request.body)
    for exp in data:
        Experts = Experience.objects.create(
            title=exp['title'],
            company=exp['company'],
            location=exp['location'],
            is_current_work_in_company=exp['is_current_work_in_company'],
            start_date=exp['start_date'],
            end_date=exp['end_date'],
            description=exp['description']
            )
        relate_id = exp['relate_id']
        freelance = RegisterFreelancer.objects.filter(id=relate_id).first()
        freelance.experience.add(Experts)

    return JsonResponse({'message': 'Add Experience data '})
@api_view(['POST'])
def addServices(request):
    fetchUser = RegisterFreelancer.objects.filter(id=int(request.data['id'])).first()
    data = request.data['services']
    for service in data:
        serv=Services.objects.filter(id=service).first()
        fetchUser.services.add(serv)

    return JsonResponse({'message': 'services added '})

@api_view(['POST'])
def addSkills(request):
    fetchUser = RegisterFreelancer.objects.filter(id=int(request.data['id'])).first()
    data = request.data['skills']
    for skill in data:
        skilll=Skills.objects.filter(id=skill).first()
        fetchUser.skills.add(skilll)

    return JsonResponse({'message': 'Skills added '})


@api_view(['POST'])
def addJobTitle(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        user.job_title=request.data['jobtitle']
        user.save()
        return JsonResponse({'message': 'Job title added'})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

