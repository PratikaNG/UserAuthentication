from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def treasure(request):
    return render(request,'treasure.html')