from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

def Topic_info(request):
    TO=TopicForm()
    d={'TO':TO}
    if request.method=="POST":
        TRD=TopicForm(request.POST)
        if TRD.is_valid():
            TRD.save()
            return HttpResponse('Data Insertd Into Topic')
    return render(request,"Topic_info.html",d)


def Webpage_info(request):
    WO=WebpageForm()
    d={"WO":WO}
    if request.method=='POST':
        WRD=WebpageForm(request.POST)
        if WRD.is_valid():
            WRD.save()
            return HttpResponse('Data Inserted Into Webpage')
    return render(request,"webpage_info.html",d)


def Access_info(request):
    AO=AccessRecordForm()
    d={'AO':AO}
    if request.method=='POST':
        ARQ=AccessRecordForm(request.POST)
        if ARQ.is_valid():
            ARQ.save()
            return HttpResponse("Data Inserted Into AccessRecords")
    return render(request,"Access_info.html",d)