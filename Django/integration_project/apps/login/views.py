from django.shortcuts import render,redirect
from models import users
from django.contrib import messages
import re
from django.contrib.auth import authenticate
import inspect
email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
import bcrypt
def containnumber(string):
    return bool(re.search(r'\d', string))

def index(request):
    context= {
        'users': users.objects.all()
    }
    return render(request, 'index.html',context)

def add(request):
    firstname = request.POST['first']
    lastname = request.POST['last']
    email = request.POST['email']
    password = request.POST['pass']
    passwordcon = request.POST['passcon']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    error = False
    context = {
        'users': users.objects.all(),
        }
    if len(firstname)<2:
        error= True
        context['enterfirst'] = 'Enter a valid name'
    if containnumber(firstname)==True:
        error = True
        context['enterfirst'] = 'Enter a valid name'
    if len(lastname)<2:
        error = True
        context['enterlast'] = 'Enter a valid name'
    if containnumber(lastname):
        error = True
        context['enterlast'] = 'Enter a valid name'
    if not email_re.match(email):
        error = True
        context['emailcon'] = 'Must be a valid email'
    if len(password)<9:
        error = True
        context['password'] = 'Password must be longer than 8 digits'
    if len(passwordcon)<9:
        error = True
        context['password'] = 'Password must be longer than 8 digits'
    if password != passwordcon:
        context['password'] = 'Passwords must match'
        error = True
    if not error:
        print pw_hash
        context['sucess'] =  'You sucessfully registerd'
        users.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email = request.POST['email'], password= pw_hash)
        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html',context)

def login(request):
    email_login = request.POST['email_login']
    password_login = request.POST['password_login']
    #pw_hash = bcrypt.hashpw(password_login.encode(), bcrypt.gensalt())
    user = users.objects.filter(email = email_login)
    #password1 = users.objects.get(password = password_login)
    hashed = user[0].password
    # print ([p.password for p in user]),passhash
    if user is not None:
        if bcrypt.hashpw(password_login.encode(), hashed.encode()) == hashed:
            print 'Worked!!!'
            return render(request, 'sucess.html')
    else:
        context = {
            'fail': 'Email and password did not match'
        }
        return render(request, 'index.html', context)
