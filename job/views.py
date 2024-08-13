from django.core.paginator import Paginator
from django.shortcuts import render
import slugify
from .models import Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj}
    return render(request, 'job\job_list.html', context)

def job_details(request, slug):
    job_details = Job.objects.get(slug=slug)
    context = {'job':job_details}
    return render(request, 'job\job_details.html', context)