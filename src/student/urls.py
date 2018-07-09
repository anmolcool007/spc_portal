from django.urls import path
from .views import DetailsView, JobOffersListView, InternshipOffersListView, ResumeUploadView

app_name = 'student'

urlpatterns = [
    path('details/', DetailsView.as_view(), name="detail"),
    path('intern_offers/', InternshipOffersListView.as_view(), name='intern-offers'),
    path('job_offers/', JobOffersListView.as_view(), name='job-offers'),
    path('resume_upload/', ResumeUploadView.as_view(), name='resume_upload'),
]
