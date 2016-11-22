from  django.shortcuts import  render
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import  login_required
from django.core.urlresolvers import reverse




@login_required()
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'index.html')
         #return HttpResponseRedirect(reverse('servers_list'))
         #return  HttpResponse('index')
         #return HttpResponseRedirect(reverse('index'))
