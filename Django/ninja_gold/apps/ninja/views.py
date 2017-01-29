from django.shortcuts import render
import random

def index(request):
    request.session['gold'] = 0
    return render(request, 'index.html')

def process(request):
    if (request.POST['action'] == 'casinomoney'):
        request.session['gold'] += random.randrange(-50,50)
        return render(request, 'index.html')
    if (request.POST['action'] == 'farmmoney'):
        request.session['gold'] += random.randrange(10,20)
        return render(request, 'index.html')
    if (request.POST['action'] == 'cavemoney'):
        request.session['gold'] += random.randrange(5,10)
        return render(request, 'index.html')
    if (request.POST['action'] == 'housemoney'):
        request.session['gold'] += random.randrange(2,5)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
