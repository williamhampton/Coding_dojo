from django.shortcuts import render

def index(request):
    return render(request, 'temp/index.html')

def registration(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return render(request, 'temp/final.html')
