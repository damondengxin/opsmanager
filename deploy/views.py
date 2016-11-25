from django.shortcuts import render
from django.http import  HttpResponse
from .models import  Deploy

# Create your views here.

def deploylist(request):
    d_list=Deploy.objects.all()
    #return  HttpResponse("test")
    return  render(request,'deploylist.html',{'d_list':d_list})

def deployadd(request):
    return render(request, 'deployadd.html')
    if request.method == 'POST':
        projectname = request.POST['projectname']
        projectaddress =request.POST['projectaddress']
        hostname=request.POST['hostname']
        hostip=request.POST['hostip']

        deploydata=Deploy(project=projectname,address=projectaddress,deployhost=hostname,hostip=hostip)
        deploydata.save()
        return  render(request,'deploylist.html')

