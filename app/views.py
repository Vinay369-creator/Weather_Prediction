from django.shortcuts import render,redirect
from app.models import *
from django.contrib import messages
import requests
from django.http import HttpResponse
from .forms import *

# Create your views here

def home(request):
    API_key='YOUR OWN API KEY '
    url=f'https://api.openweathermap.org/data/2.5/weather?q={{}}&appid={API_key}'
    if request.method=='POST':
        wd=weatherdf(request.POST)
        if wd.is_valid():
            cname=wd.cleaned_data['name']
            wc=City.objects.filter(name=cname).count()
            if wc == 0:
                res=requests.get(url.format(cname))
                if res.status_code==200:
                    wd.save()
                    messages.success(request,'city added successfully')
                else:
                    messages.error(request,'invalid city')
            else:
                messages.error(request,'city is already present')

    ewo=weatherdf()
    cities=City.objects.all()
    d={}
    l=[]
    for city in cities:
        res=requests.get(url.format(city.name))
        if res.status_code==200:
            data=res.json()
            con={
                'name':city.name,
                'wet':data['weather'][0]['description'],
                'logo':data['weather'][0]['icon'],
                'tem':data['main']['temp'], }
            l.append(con)
    d={'cdata':l,'ewo':ewo}              
    return render(request,'home.html',d)



def delete_city(request,name):
    City.objects.filter(name=name).delete()
    return redirect('/home/')

    
