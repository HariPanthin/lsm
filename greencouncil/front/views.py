from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'front/index.html')
    
def services(request):
    return render(request,'front/services.html')

def funding(request):
    return render(request, 'front/funding.html')

def resources(request):
    return render(request, 'front/resources.html')
    