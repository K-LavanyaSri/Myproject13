from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def products(request):
    return render(request,'products.html')

def testimonials(request):
    return render(request,'testimonials.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

def contactUs(request):
    return render(request,'contactUs.html')