from django.shortcuts import render, HttpResponse
def clock(request):
    context = {
    "somekey":"somevalue"
    }
    return render(request,'time/index.html')
