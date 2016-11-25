from django.conf.urls import url

from . import  views

urlpatterns = [
    url(r'deploylist',views.deploylist,name='deploylist'),
    url(r'deployadd',views.deployadd,name='deployadd'),
]