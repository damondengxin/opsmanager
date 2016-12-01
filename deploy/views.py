from django.shortcuts import render
from django.http import  HttpResponse
from .models import  Deploy

# Create your views here.

def deploylist(request):
    d_list=Deploy.objects.all()
    #return  HttpResponse("test")
    return  render(request,'deploylist.html',{'d_list':d_list})

def deployadd(request):
    if request.method == 'POST':
        project = request.POST['projectname']
        address =request.POST['projectaddress']
        hostname=request.POST['hostname']
        hostip=request.POST['hostip']

        deploydata=Deploy(project=project,address=address,deployhost=hostname,hostip=hostip,status=1)
        deploydata.save()
        return  render(request,'deploylist.html')

    return render(request, 'deployadd.html')


def deployinfo(request):
    return  render(request,'deployinfo.html')