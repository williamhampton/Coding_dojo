from django.shortcuts import render,redirect
from . import models
from models import Users, Admins
from django.db.models import Count
from django.contrib import messages
import re
from django.contrib.auth import authenticate
import inspect
email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
import bcrypt
def containnumber(string):
    return bool(re.search(r'\d', string))
def index(request):
    return render(request,'index.html')
def register(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'register.html', context)

def login(request):
    return render(request, 'login.html')

def login_login(request):
    email_login = request.POST['email_login']
    print Users.objects.filter(email = request.POST['email_login']).exists()

    if Users.objects.filter(email = request.POST['email_login']).exists() == False:
        context = {
            'fail': 'Enter a valid email'
        }
        return render(request, 'index.html',context)
    else:
        password_login = request.POST['password_login']
        user = Users.objects.filter(email = email_login)
        hashed = user[0].password
        if user is not None:
            if bcrypt.hashpw(password_login.encode(), hashed.encode()) == hashed:
                print user[0].first_name
                request.session['first_name'] = user[0].first_name
                request.session['last_name'] = user[0].last_name
                request.session['email'] = user[0].email
                request.session['id'] = user[0].id
                return redirect('/dashboard')
            else:
                context = {
                'fail': 'Email and password did not match'
                }
                return render(request, 'register.html', context)

def register_create(request):
    firstname = request.POST['first_name']
    lastname = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    passwordcon = request.POST['password_con']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    error = False
    context = {
        'users': Users.objects.all(),
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
        Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password= pw_hash)
        print len(Users.objects.all())
        if len(Users.objects.all()) == 1:
            Admins.objects.create(member = Users.objects.all().filter(first_name = request.POST['first_name'])[0])
            print Users.objects.all().filter(first_name = request.POST['first_name'])[0].id
        return render(request, 'register.html',context)
    else:
        return redirect('/login')

def dashboard(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'dashboard.html', context)

def dashboard_admin(request):
    context = {
        'users': Users.objects.all(),
        'admins': Admins.objects.all()
    }
    return render(request, 'dashboard_admin.html', context)

def user_delete(request,id):
    Users.objects.all().filter(id = id).delete()
    return redirect('/dashboard/admin')
