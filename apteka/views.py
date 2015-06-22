from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from apteka.forms import AptekaForm
# Create your views here.

def all_apteks(request):
    return render(request, 'apteka/all_apteks.html')

def add_apteks(request):
    if request.method == 'POST':
        form = AptekaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/apteka/add_process')
    else:
        form = AptekaForm()

    return render(request, 'apteka/add_apteks.html', {'form':form})

def add_apteks_process(request):
    name = request.POST['name']
    phone = request.POST['phone']
    address = request.POST['address']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    return render(request, 'apteka/add_apteks_process.html',
        {'name' : name, 'phone' : phone, 'address':address, 'latitude':latitude, 'longitude':longitude})
