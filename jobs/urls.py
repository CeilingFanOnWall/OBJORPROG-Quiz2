from django.urls import path
from .views import job_list, account_home
from . import views
app_name = 'jobs'

urlpatterns = [
    path('', views.jobs_home, name='jobs_home'),
    path('listings/', views.listings, name='listings'),
    path('<int:pk>/', views.job_detail, name='job_detail'),  # Add this line
    path('<int:job_id>/apply/', views.apply, name='apply'),
    path('application-success/', views.application_success, name='application_success'),
]