import base64
from datetime import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import Skills, RegisterFreelancer
from home_app.models import Job, LikeJob, DisLike
from home_app.serlializers import JobSerializer
from profile_app.models import Portflio, Certification
# Create your views here.
from datetime import date

from authentication.models import RegisterUser
from home_app.models import JobImages

today = date.today()


@api_view(['POST'])
def details_free_home(request):
    user = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        education = user.education.all()
        experience = user.education.all()
        portflio = Portflio.objects.filter(portflio_freelancer=user.id)
        certification = Certification.objects.filter(certification_user_freelancer=user.id)
        completeness = 0
        if education:
            completeness = completeness + 25
        if experience:
            completeness = completeness + 25
        if portflio:
            completeness = completeness + 25
        if certification:
            completeness = completeness + 25
        jobs = Job.objects.all()

        return Response({
            "fname": user.first_name,
            "lname": user.last_name,
            "jobtitle": user.job_title,
            "image": user.user_image.url,
            "completeness": completeness,
            "date_now": today.strftime("%B %d, %Y"),
            "jobs": JobSerializer(jobs, many=True).data

        })
    else:
        return Response('not found')

@api_view(['POST'])
def like_job(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        job=Job.objects.filter(id=request.data['job_id']).first()
        like=LikeJob.objects.create(id_free=user)
        job.likes.add(like)
        job.save()
        return  Response({"res":"ok","id":like.id})
    else:
        return  Response('not found')

@api_view(['POST'])
def removelike_job(request):
        like_id=LikeJob.objects.filter(id=request.data['like_id']).first()
        if like_id:
            like_id.delete()
            return  Response('ok')
        else:
            return  Response('not found')

@api_view(['POST'])
def removeDislike_job(request):
        like_id=DisLike.objects.filter(id=request.data['like_id']).first()
        if like_id:
            like_id.delete()
            return  Response('ok')
        else:
            return  Response('not found')

@api_view(['POST'])
def Dislike_job(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        job=Job.objects.filter(id=request.data['job_id']).first()
        dis=DisLike.objects.create(id_free=user)
        job.dislikes.add(dis)
        job.save()
        return  Response({"res":"ok","id":dis.id})
    else:
        return  Response('not found')


@api_view(['POST'])
def AddJobClient(request):
    print(request.data)
    client_id=request.data['client_id']
    user =RegisterUser.objects.filter(id=client_id).first()
    if user:
        images = request.FILES.getlist('images')
        Jobs = Job.objects.create(
            title= request.data['title'],
            cost = request.data['cost'],
            description = request.data['description'],
            is_pyment = request.data['is_pyment'],
            client_id=user
        )
        for img in images :
            jobImage = JobImages.objects.create(image=img)
            Jobs.images.add(jobImage),
        return Response('ok')
    else:
        return Response('not added')



