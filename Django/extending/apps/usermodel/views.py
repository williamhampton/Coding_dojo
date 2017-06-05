from django.shortcuts import render
from .forms import registration
from datetime import date

def index(request):
    form = registration()
    context = {
        'form': form
    }
    return render(request, 'index.html',context)

def sucess(request):
    born = request.POST.get('age')
    print born
    print '*'*50
    if int(born) < 15:
        return render (request, 'failure.html')
    else:
        return render(request, 'sucess.html')
