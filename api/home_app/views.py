from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import Skills, RegisterFreelancer
from home_app.models import Job, LikeJob, DisLike, notificationsClient, SendApply, ImagesSendApply, Hires, \
    ReviewAndRate, notificationsFree
from home_app.serlializers import JobSerializer, NotificationClientSerializer, ApplaySerializer, HireSerializer, \
    NotificationFreeSerializer
from profile_app.models import Portflio, Certification, WorkHistory
# Create your views here.
from datetime import date

from authentication.models import RegisterUser
from home_app.models import JobImages
from profile_app.serlializers import portfiloSerialzer

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
            if not j.is_hire:
                jobs_skils=list(j.skills.values_list('name', flat=True))
                ins=set(skills_usr) & set(jobs_skils)
                if ins:
                    jobs_send.append(j)
        my_applay=SendApply.objects.filter(free=user)
        jobsAllay=[]
        for j in my_applay:
            jobsAllay.append(j.job.id)
        return Response({
            "fname": user.first_name,
            "lname": user.last_name,
            "jobtitle": user.job_title,
            "image": user.user_image.url,
            "completeness": completeness,
            "date_now": today.strftime("%B %d, %Y"),
            "jobs": JobSerializer(jobs_send, many=True).data,
            "jobsAllay":jobsAllay
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
        job_sen=[]
        for j in jobs:
            if not j.is_hire:
                job_sen.append(j)
        return  Response(JobSerializer(job_sen,many=True).data)
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
            "numDislike":numDislike,
            'client_id': job.client_id.id,
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
        if not j.is_hire:
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
        if not j.is_hire:
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
        if not j.is_hire:
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
        if not j.is_hire:
            for w in words:
                if  w in list(j.skills.values_list('name', flat=True)):
                    job_send.append(j)
    return Response(JobSerializer(job_send, many=True).data)

@api_view(['POST'])
def getnotificationsClient(request):
    user=RegisterUser.objects.filter(id=request.data['id']).first()
    if user:
        notifications=notificationsClient.objects.filter(user_revoker=user)
        return  Response(NotificationClientSerializer(notifications,many=True).data)
    else:
        return Response({'not found'})

@api_view(['POST'])
def getnotificationsFree(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        notifications=notificationsFree.objects.filter(user_revoker=user)
        return  Response(NotificationFreeSerializer(notifications,many=True).data)
    else:
        return Response({'not found'})


@api_view(['POST'])
def add_applay(request):
    free=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    job =Job.objects.filter(id=request.data['id_job']).first()
    if free and job:
       send= SendApply.objects.create(
           free=free,
           job=job,
           cover=request.data['cover'],
           cost_re=request.data['cost_re'],
           cost_comp=request.data['cost_comp']
       )
       images = request.FILES.getlist('images[]')
       for img in images:
            jobImage = ImagesSendApply.objects.create(image=img)
            send.images.add(jobImage)
            job.Proposals.add(free)
       return Response('ok')
    else:
        return Response("not found")
@api_view(['POST'])
def makeNotificationClientRead(request):
    user=RegisterUser.objects.filter(id=request.data['id']).first()
    if user:
        nts=notificationsClient.objects.filter(user_revoker=user)
        for n in nts:
            n.status="read"
            n.save()
        notifications = notificationsClient.objects.filter(user_revoker=user)
        return Response(NotificationClientSerializer(notifications, many=True).data)
    else:
        return Response("not found")

@api_view(['POST'])
def makeNotificationFreetRead(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        nts=notificationsFree.objects.filter(user_revoker=user)
        for n in nts:
            n.status="read"
            n.save()
        notifications = notificationsFree.objects.filter(user_revoker=user)
        return Response(NotificationFreeSerializer(notifications, many=True).data)
    else:
        return Response("not found")

@api_view(['POST'])
def deletNotificationClient(request):
    no=notificationsClient.objects.filter(id=request.data['id']).first()
    if no:
        no.delete()
        return Response('ok')
    else:
        return Response("not found")

@api_view(['POST'])
def deletNotificationFree(request):
    no=notificationsFree.objects.filter(id=request.data['id']).first()
    if no:
        no.delete()
        return Response('ok')
    else:
        return Response("not found")

@api_view(['POST'])
def get_jobs_proposals(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        applayes=SendApply.objects.filter(free=user)
        jobs=[]
        for app in applayes:
            if not app.is_hire:
                jobs.append(app.job)
        return Response(JobSerializer(jobs,many=True).data)
    else:
        return Response('not found')

@api_view(['POST'])
def jobs_hire(request):
    user = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        hires = Hires.objects.filter(free=user)
        jobs = []
        for h in hires:
            if not h.is_payment:
                jobs.append(h.job)
        return Response(JobSerializer(jobs, many=True).data)
    else:
        return Response('not found')
@api_view(['POST'])
def job_cover(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    job=Job.objects.filter(id=request.data['id_job']).first()
    if user and job:
        cover=SendApply.objects.filter(free=user,job=job).first()
        return Response(ApplaySerializer(cover).data)
    else:
        return  Response("not found")
@api_view(['POST'])
def job_hire_de(request):
    user = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    job = Job.objects.filter(id=request.data['id_job']).first()
    if user and job:
        hire=Hires.objects.filter(free=user,job=job).first()
        return Response(HireSerializer(hire).data)
    else:
        return  Response("not found")
@api_view(['POST'])
def finish_job(request):
    hire=Hires.objects.filter(id=request.data['id']).first()
    if hire:
        hire.is_finish=True
        hire.save()
        return Response('ok')
    else:
        return Response("not found")
@api_view(['POST'])
def get_portfolio(request):
    p=Portflio.objects.filter(id=request.data['id']).first()
    if p:
        return  Response(portfiloSerialzer(p).data)
    else:
        return Response("not found")

@api_view(['POST'])
def hire(request):
    user=RegisterUser.objects.filter(id=request.data['user']).first()
    free=RegisterFreelancer.objects.filter(id=request.data['free']).first()
    app=SendApply.objects.filter(id=request.data['job']).first()
    job=Job.objects.filter(id=app.job.id).first()
    cost=request.data['cost']
    if user and free and job:
        hire=Hires.objects.create(client=user,free=free,job=job,cost=cost)
        job.is_hire=True
        job.save()
        app.is_hire=True
        app.save()
        return Response('ok')
    else:
        return Response("not found")
@api_view(['POST'])
def get_jobs_hire_client(requests):
    user=RegisterUser.objects.filter(id=requests.data['id']).first()
    if user:
        hires=Hires.objects.filter(client=user,is_finish=False)
        return  Response(HireSerializer(hires,many=True).data)
    else:
        return Response("not found")
@api_view(['POST'])
def get_jobs_finish_client(requests):
    user = RegisterUser.objects.filter(id=requests.data['id']).first()
    if user:
        hires = Hires.objects.filter(client=user, is_finish=True,is_payment=False)
        return Response(HireSerializer(hires, many=True).data)
    else:
        return Response("not found")
@api_view(['POST'])
def addReview(requests):
    user = RegisterFreelancer.objects.filter(id=requests.data['id']).first()
    client =RegisterUser.objects.filter(id=requests.data['client']).first()
    if user and client:
        ReviewAndRate.objects.create(free=user,review=requests.data['review'],rate=requests.data['rate'])
        h= Hires.objects.filter(id=requests.data['job_id']).first()
        h.is_payment=True
        h.save()
        WorkHistory.objects.create(work_history_client=client,work_history_freelancer=user,location=h.job.title,cost=h.cost)
        return Response('ok')
    else:
        return Response('not found')