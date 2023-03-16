from .models import RegisterFreelancer, RegisterUser, Experience, Services, Skills
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .serlializers import *
from .tokens import account_activation_token, Reg_Token
from .models import RegisterFreelancer
from .serlializers import SignUpFreelancerSerializer
from .tokens import account_activation_token
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from django.utils.encoding import force_str
import json
from django.http import JsonResponse
from .models import Education
from .tokens import account_activation_token
from rest_framework.decorators import api_view

@api_view(['POST'])
def signup_freeLancer(request):
    user = SignUpFreelancerSerializer(data=request.data)
    if user.is_valid():
        hashedpassword = make_password(user.data['password'])
        register=RegisterFreelancer.objects.create(first_name=user.data['first_name'],
                                         last_name=user.data['last_name'],email=user.data['email'],
                                         password=hashedpassword,phone_number=user.data['phone_number'],
    )

        mail_subject = 'Activation link has been sent to your email id'
        messages = "http://localhost:3000/activate_free/" + str(
            urlsafe_base64_encode(force_bytes(register.id))) + "/" + account_activation_token.make_token(register)

        print(messages)

        #to_email = [user.data['email']]
        #from_email = settings.EMAIL_HOST_USER
        #send_mail(mail_subject, messages, from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def registerUserSerialzer(request):
    user = SignUpUserSerialzer(data=request.data)
    if user.is_valid():
        hashPassword = make_password(user.data['password'])
        input = RegisterUser.objects.create(fname=user.data['fname'], lname=user.data['lname'],
                                            email=user.data['email'],
                                            password=hashPassword, phone=user.data['phone'])

        mail_subject = 'Activation link has been sent to your email id'
        messages = "http://localhost:3000/activate_user/" + str(
            urlsafe_base64_encode(force_bytes(input.id))) + "/" + Reg_Token.make_token(input)

        print(messages)

       # to_email = [user.data['email']]
       # from_email = settings.EMAIL_HOST_USER
        #send_mail(mail_subject, messages, from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def verfy_email_free(request):
    print(request.data)
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterFreelancer.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):
        user.is_active=True
        user.save()
        return Response({'res':'ok','id':user.id})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def verfy_email_register(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterUser.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):
        user.is_active = True
        user.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def emailResetPassword(request):
    email = request.data.get('email')
    type=''
    if not email:
        return Response({'error': 'Email is required.'}, status=400)

    user = RegisterFreelancer.objects.filter(email=email).first()
    if not user:
        user = RegisterUser.objects.filter(email=email).first()
        if not user:
            return Response({'not'})
        else:
            type='user'
    else:
        type='free'

    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.id))
    reset_url = f'http://127.0.0.1:3000/test_token/{uid}/{token}/{type}'
    print(reset_url)
    #send_mail(
    #    'Password Reset',
    #    f'Click the following link to reset your password: {reset_url}',
     #   'soonfu0@gmail.com',
     #   [email],
     #   fail_silently=False,
   # )

    return Response('ok', status=200)

@api_view(['POST'])
def reset_password_View(request):
    print(request.data)
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterFreelancer.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):
        return Response({'id':user.id})
    else:
        return JsonResponse({'error': 'Invalid password reset token.'})

        # return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save_education(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for education_data in data:
            education = Education.objects.create(
                school=education_data['school'],
                degree=education_data['degree'],
                study=education_data['study'],
                from_year=education_data['from_year'],
                to_year=education_data['to_year'],
                description=education_data['description']
            )

            freelancer_register_id = education_data['freelancer_register_id']
            freelancer_register = RegisterFreelancer.objects.filter(id=freelancer_register_id).first()
            freelancer_register.education.add(education)
        freelancer_register.save()

        return JsonResponse({'message': 'Educations saved successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@api_view(['POST'])
def save_overview(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        registerFreelancer = RegisterFreelancer.objects.filter(id=data['id']).first()
        registerFreelancer.overview = data['overview']
        registerFreelancer.save()
        return JsonResponse({'id': registerFreelancer.id})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)


@api_view(['POST'])
def rest_password_view_user(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterUser.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):

        return Response({'id':user.id})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login(request):
    email= request.data['email']
    password=request.data['password']

    user_free=RegisterFreelancer.objects.filter(email=email).first()
    if user_free:
        if check_password(password,user_free.password):
            if user_free.is_active:
                if user_free.is_complete_date:
                    return Response({'ress':'ok',"id": user_free.id,"name":user_free.first_name+' '+user_free.last_name})
                else:
                    return Response({'ress':'not complete'})
            else:
                return Response({"ress": 'not active',"id": user_free.id,"name":user_free.first_name+' '+user_free.last_name})
        else:
            return Response({"ress": 'password worng'})
    else:
        user_free=RegisterUser.objects.filter(email=email).first()
        if user_free:
            if check_password(password, user_free.password):
                if user_free.is_active:
                    return Response({'ress':'ok',"id": user_free.id,"name":user_free.fname+' '+user_free.lname})
                else:
                    return Response({"ress": 'not active'})
            else:
                return Response({"ress": 'password worog'})
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
    freelance.save()

    return JsonResponse({'message': 'Add Experience data '})
@api_view(['POST'])
def addServices(request):
    fetchUser = RegisterFreelancer.objects.filter(id=int(request.data['id'])).first()
    data = request.data['services']
    for service in data:
        serv=Services.objects.filter(id=service).first()
        fetchUser.services.add(serv)
    fetchUser.save()

    return JsonResponse({'message': 'services added '})

@api_view(['POST'])
def addSkills(request):
    fetchUser = RegisterFreelancer.objects.filter(id=int(request.data['id'])).first()
    data = request.data['skills']
    for skill in data:
        skilll=Skills.objects.filter(id=skill).first()
        fetchUser.skills.add(skilll)
    fetchUser.save()
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


@api_view(['GET'])
def view_service_serializer(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Services.objects.filter(**request.query_params.dict())
    else:
        items = Services.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = ServicesSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_skills_serializer(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Skills.objects.filter(**request.query_params.dict())
    else:
        items = Skills.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = SkillsSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def check_email(request) :
    email = request.data['email']
    user = RegisterFreelancer.objects.filter(email=email).first()
    if user:
        return Response('ok')
    else:
        user = RegisterUser.objects.filter(email=email).first()
        if user:
            return Response('ok')
        else:
            return Response('not found')

@api_view(['POST'])
def add_address(request):
    id = request.data['id']
    user = RegisterFreelancer.objects.filter(id=id).first()
    if user:
        user.street_address=request.data['street_address']
        user.city=request.data['city']
        user.state=request.data['state']
        user.postal_code=request.data['postal_code']
        user.is_complete_date=True
        user.save()
        return Response('add address')
    else:
        return  Response('not found')

@api_view(['POST'])
def set_password(request):
    if(request.data['type']=='user'):
        user=RegisterUser.objects.filter(id=request.data['id']).first()
        if user:
            user.password=make_password(request.data['password'])
            user.save()
            return Response('ok')
        else:
            return  Response('not found')
    else:
        user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
        if user:
            user.password=make_password(request.data['password'])
            user.save()
            return Response('ok')
        else:
            return  Response('not found')