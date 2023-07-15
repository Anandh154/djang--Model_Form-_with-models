from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def person(request):
    PMFO=PersonModelForm()
    d={'PMFO':PMFO}
    if request.method=='POST':
        PMFOD=PersonModelForm(request.POST)
        if PMFOD.is_valid():
            PMFOD.save()
            return HttpResponse('insertion is done')
        else:
            return HttpResponse('invalid data')
    return render(request,'person.html',d)