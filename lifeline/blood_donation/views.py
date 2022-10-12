from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blood_donation/html/home.html')
