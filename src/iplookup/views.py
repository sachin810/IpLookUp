from django.conf import settings
from django.shortcuts import render
import requests
from .forms import IpForm
from .config import ACCESS_KEY

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    data = response.json()
    form  = IpForm(request.POST or None)
    if form.is_valid():

        ip = form.cleaned_data['ip']
        response = requests.get('http://api.ipstack.com/'+ ip +'?access_key=' + ACCESS_KEY)
        geodata = response.json()
        return render(request, 'result.html', {
            'ip': geodata['ip'],
            'country': geodata['country_name'],
            "city": geodata['city'],
           ''' "hostname":geodata['hostname'],'''
            'type':geodata["type"],
            "continent_code":geodata["continent_code"],
            "continent_name": geodata["continent_name"],
            "country_name":geodata['country_name'],
            "region_name":geodata['region_name'],
            "country_code":geodata['country_code'],
            "zip":geodata['zip'],
            "region_code":geodata['region_code'],
            'form': form,

        })
    return render(request, 'home.html', {
        'form': form,
        'ip': data['ip'],
        'country': data['country_name'],
         }  )
