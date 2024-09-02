from django.urls import path
from . import views

urlpatterns = [
    path('jobs', views.JobListCreateView.as_view(), name='job-listcreate'),
    path('jobs/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),
    path('applicants', views.JobApplicantListCreateView.as_view(), name='job_applicant-listcreate'),
    path('applicants/<int:pk>', views.JobApplicantDetailView.as_view(), name='job_applicant-detail'),
]

