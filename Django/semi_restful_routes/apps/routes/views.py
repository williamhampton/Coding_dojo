from django.shortcuts import render,redirect
from . import models


def index(request):
    products = models.products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'add.html')

def create(request):
    models.products.objects.create(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
    return redirect('/products')

def destroy(request, id):
    product_id = models.products.objects.filter(id = id)
    models.products.objects.filter(id=id).delete()
    return redirect('/products')

def show(request, id):
    products = models.products.objects.filter(id = id)
    context = {
        'products': products
    }
    return render(request, 'show.html', context)

def edit(request,id):
    context = {
    'id': id
    }
    return render(request, 'edit.html',context)

def update(request,id):
    models.products.objects.filter(id=id).delete()
    models.products.objects.create(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'], id = id)
    return redirect('/products')
