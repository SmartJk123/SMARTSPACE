from django.shortcuts import render

def home(request):
    return render(request, 'app/homepage.html')

def addproperty(request):
    return render(request, 'addproperty.html')
