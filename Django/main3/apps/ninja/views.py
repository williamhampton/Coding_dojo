from django.shortcuts import render

def index(request):
    return render(request, 'temp/index.html')

def ninjas(request):
    return render(request, 'temp/ninjas.html')

def ninja(request, color):
    context = {
        'color': color
    }
    if context['color'] == 'blue':
        return render(request, 'temp/ninja.html', context)
    else:
        return render(request, 'temp/ninja.html', context)
