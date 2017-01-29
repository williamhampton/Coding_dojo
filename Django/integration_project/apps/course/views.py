from django.shortcuts import render,redirect
from models import courses

def index(request):
    context = {
        'courses': courses.objects.all()
    }
    return render(request, 'index.html',context)

def add(request):
    courses.objects.create(course= request.POST['course1'], description= request.POST['description1'])
    return redirect('/')

def remove(request, id):
    course_id = courses.objects.get(id = id)
    courses.objects.filter(id=id).delete()
    return redirect('/')
