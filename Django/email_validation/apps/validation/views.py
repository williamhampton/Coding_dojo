from django.shortcuts import render,redirect
from models import emails
import re
email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def index(request):
    return render(request, 'index.html')

def add(request):
    email1 = request.POST['test']
    if email_re.match(email1):
        emails.objects.create(email = request.POST['test'])
        return redirect('/sucess')
    else:
        context = {
            'failures': 'That was not a valid email!!'
        }
        return render(request,'index.html', context)
def sucess(request):
    context = {
        'emails': emails.objects.all()
    }
    return render(request, 'sucesss.html',context)
def remove(request, id):
    email_id = emails.objects.get(id = id)
    emails.objects.filter(id=id).delete()
    return redirect('/sucess')
