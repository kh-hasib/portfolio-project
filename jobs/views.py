from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.http import FileResponse, Http404

def home(request):
    jobs = Job.objects.all().order_by('id')
    return render(request, 'jobs/home.html', {'jobs':jobs})

# def resume(request):
#     return render(request, 'jobs/resume.html')



def resume(request):
    try:
        return FileResponse(open('portfolio/static/resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
