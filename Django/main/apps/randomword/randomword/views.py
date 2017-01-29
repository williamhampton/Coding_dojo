from django.shortcuts import render, HttpResponse, redirect
def word(request):
    context = {
    "somekey":"somevalue"
    }
    request.session['times'] += 1
    return render(request,'pages/index.html')

def reload(request):
    request.session['times'] +=1
    return redirect('/')
