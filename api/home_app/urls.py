from django.urls import path

from .views import  *

urlpatterns = [
    path('detalis_free_home/',details_free_home),
    path('like_job/',like_job),
    path('dislike_job/',Dislike_job),
    path('removelike_job/',removelike_job),
    path('removeDislike_job/',removeDislike_job),
    path('JobClient/',AddJobClient,name='JobClient'),
]
