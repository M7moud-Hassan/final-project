from django.urls import path

from .views import  *

urlpatterns = [
    path('detalis_free_home/',details_free_home),
    path('like_job/',like_job),
    path('dislike_job/',Dislike_job),
    path('removelike_job/',removelike_job),
    path('removeDislike_job/',removeDislike_job),
    path('JobClient/',AddJobClient,name='JobClient'),
    path('job_search/',search_jobs),
    path('All_of_these_words/',All_of_these_words),
    path('The_exact_phrase/',The_exact_phrase),
    path('Skills_Search/',Skills_Search),
    path('latestJobs/',clientLatestJobs,name='latestJobs'),
    path('jobDetails/',jobDetails),
    path('add_applay/',add_applay),
    path('getnotificationsClient/',getnotificationsClient),
    path('makeNotificationClientRead/',makeNotificationClientRead),
    path('deletNotificationClient/',deletNotificationClient),
    path('get_jobs_proposals/',get_jobs_proposals),
    path('jobs_hire/',jobs_hire),
    path('job_cover/',job_cover),
    path('job_hire_de/',job_hire_de),
    path('finish_job/',finish_job),
    path('get_portfolio/',get_portfolio)
]
