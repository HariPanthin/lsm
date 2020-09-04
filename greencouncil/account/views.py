from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'account/index.html')

def signup(request):
    return render(request, 'account/signup.html')

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    pass


