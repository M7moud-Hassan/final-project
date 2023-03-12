from django.shortcuts import render

# Create your views here.
def check_email_freelancer(request) :
    email = request.data['email']
    user = RegisterFreelancer.objects.filter(email=email).first()
    if user:
        return response('ok')
    else:
        return not found


def check_email_user(request) :
    email = request.data['email']
    user = RegisterUser.objects.filter(email=email).first()
    if user:
        return response('ok')
    else:
        return not found