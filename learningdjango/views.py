# from django.http import HttpResponse
# def homepage(request):
#     return HttpResponse("you are on the home page")
# def about(request):
#     return HttpResponse("eh this part is so boring none volunteered to do it for us")
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
