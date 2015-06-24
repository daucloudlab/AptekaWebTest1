from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
# Create your views here.

def all_apteks(request):
    return render(request, 'apteka/all_apteks.html')

def add_apteks(request):
    return render(request, 'apteka/add_apteks.html')

def del_apteks(request):
    return render(request, 'apteka/del_apteks.html')

def update_apteks(request, id):
    return render(request, 'apteka/update_apteks.html', {'id':id})


