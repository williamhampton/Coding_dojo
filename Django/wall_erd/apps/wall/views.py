from django.shortcuts import render
from .models import users
def index(request):
    return render(request, "index.html")
# Create your views here.
