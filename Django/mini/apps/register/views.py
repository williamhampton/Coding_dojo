from django.shortcuts import render,redirect
from .forms import registration
# Create your views here.
def index(request):
    form = registration()
    context = {
        'form': form
    }
    return render(request, 'index.html',context)

def register(request):
    if request.method=="POST":
        form = registration(request.POST)
        print form.is_valid()
        print form.errors
    return redirect('/')
