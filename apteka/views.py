from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from apteka.forms import AptekaForm
# Create your views here.

def all_apteks(request):
    return render(request, 'apteka/all_apteks.html')

def add_apteks(request):
    return render(request, 'apteka/add_apteks.html')

