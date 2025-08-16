from django.shortcuts import render, get_object_or_404
from .models import Job
from accounts.views import register
from accounts.views import profile
from django.http import HttpResponse
from django.shortcuts import redirect


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

def account_home(request):
    return HttpResponse("Jobs Home Page")

def apply(request, job_id):
    return redirect('jobs:job_detail', pk=job_id)

def jobs_home(request):
    return render(request, 'accounts/base.html')

def listings(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def application_success(request):
    return render(request, 'jobs/application_success.html')