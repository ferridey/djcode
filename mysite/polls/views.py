from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello,world. you're at the polls index.")
