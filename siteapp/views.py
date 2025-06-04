from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def wisc(request):
    return render(request, 'wisc.html')

def planos(request):
    return render(request, 'planos.html')

def login_register(request):
    return render(request, 'login_register.html')

def index_page(request):
    return render(request, 'index.htm')
