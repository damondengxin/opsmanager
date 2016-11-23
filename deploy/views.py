from django.shortcuts import render
from django.http import  HttpResponse
from .models import  Deploy

# Create your views here.

def deploylist(request):
    d_list=Deploy.objects.all()
    #return  HttpResponse("test")
    return  render(request,'deploylist.html',{'d_list':d_list})