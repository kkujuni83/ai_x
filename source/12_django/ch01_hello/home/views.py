from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  # ✅ 이 줄 꼭 추가해야 함

def home(request):
    return HttpResponse("<h1>Hello, Django(장고)!</h1>")
