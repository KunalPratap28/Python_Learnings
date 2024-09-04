from django.shortcuts import render

# Create your views here.
def App(request):
    return render(request,'index.html')
