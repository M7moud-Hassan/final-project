import base64
import json
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
        skills_usr=list(user.skills.values_list('name', flat=True))
        jobs_send=[]
        for j in jobs:
            jobs_skils=list(j.skills.values_list('name', flat=True))
            ins=set(skills_usr) & set(jobs_skils)
            if ins:
                jobs_send.append(j)
        return Response({
            "fname": user.first_name,
            "lname": user.last_name,
            "jobtitle": user.job_title,
            "image": user.user_image.url,
            "completeness": completeness,
            "date_now": today.strftime("%B %d, %Y"),
            "jobs": JobSerializer(jobs_send, many=True).data

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
        print(request.data)
        like_id=LikeJob.objects.filter(id=request.data['like_id']).first()
        if like_id:
            like_id.delete()
            return  Response('ok')
        else:
            return  Response('not found')

@api_view(['POST'])
def removeDislike_job(request):
        print(request.data)
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
        images = request.FILES.getlist('images[]')
        Jobs = Job.objects.create(
            title= request.data['title'],
            cost = request.data['cost'],
            description = request.data['description'],
            is_pyment = True if request.data['is_pyment']=='true' else False,
            client_id=user
        )
        for img in images:
            jobImage = JobImages.objects.create(image=img)
            Jobs.images.add(jobImage)

        for sk in request.data.getlist('skills[]'):
            us=Skills.objects.filter(id=sk).first()
            Jobs.skills.add(us)
            Jobs.save()
        return Response('ok')
    else:
        return Response('not added')



@api_view(['POST'])
def clientLatestJobs(request):
    client=RegisterUser.objects.filter(id=request.data['client_id']).first()
    if client:
        jobs=Job.objects.filter(client_id=client)
        return  Response(JobSerializer(jobs,many=True).data)
    else:
        return Response('not found')

@api_view(['POST'])
def jobDetails(request):
    job=Job.objects.filter(id=request.data['id']).first()
    if job:
        images=[]
        for im in job.images.all():
            images.append(im.image.url)
        skills=[]
        for sk in job.skills.all():
            skills.append(sk.name)
        proposals=[]
        for p in  job.Proposals.all():
            proposals.append({
                "id":p.id,
                "name":f'{p.first_name} {p.last_name}',
                "image":p.user_image.url
            })
        numlikes=len(job.likes.all())
        numDislike=len(job.dislikes.all())
        return Response({
            "title":job.title,
            "create_at":job.create_at,
            'cost':job.cost,
            "images":images,
            "description":job.description,
            "skills":skills,
            "proposals":proposals,
            "numlikes":numlikes,
            "numDislike":numDislike
        })
    else:
        return  Response('not found')

@api_view(['POST'])
def search_jobs(request):
    word=request.data['word']
    words = word.split()
    jobs=Job.objects.all()
    job_send=[]
    for j in jobs:
        for w in words:
            if w in j.title or w in j.description or w in list(j.skills.values_list('name', flat=True)):
                job_send.append(j)
    return Response(JobSerializer(job_send,many=True).data)
@api_view(['POST'])
def All_of_these_words(request):
    word=request.data['word']
    words = word.split()
    jobs=Job.objects.all()
    job_send=[]
    for j in jobs:
        title = j.title.split()
        des=j.description.split()
        if all(wor in title for wor in words) or all(wor in des for wor in words):
            job_send.append(j)
    return Response(JobSerializer(job_send,many=True).data)
@api_view(['POST'])
def The_exact_phrase(request):
    word = request.data['word']
    jobs = Job.objects.all()
    job_send = []
    for j in jobs:
        if word in j.title or word in j.description:
            job_send.append(j)
    return Response(JobSerializer(job_send, many=True).data)

@api_view(['POST'])
def Skills_Search(request):
    word = request.data['word']
    words = word.split()
    jobs = Job.objects.all()
    job_send = []
    for j in jobs:
        for w in words:
            if  w in list(j.skills.values_list('name', flat=True)):
                job_send.append(j)
    return Response(JobSerializer(job_send, many=True).data)
