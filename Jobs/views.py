from django.shortcuts import render
from .models import Job

# Create your views here.
def homepage(request):
    return render(request, 'Jobs/home.html')

def projects(request):
    # fetch all the objects of the job
    job = Job.objects
    return render(request, 'Jobs/projects.html', {'job':job})
