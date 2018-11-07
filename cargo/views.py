from django.shortcuts import render


def indexpage(request):
    return render(request,'cargo/index.html')

def base(request):
    return render(request,'cargo/base.html')

def car(request):
    return render(request,'cargo/car.html')
