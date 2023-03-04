from django.shortcuts import render

# Create your views here.

def index(request):
    print("render index function called")
    return render(request, 'index.html')