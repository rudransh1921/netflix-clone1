from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from service.models import Solo
from new.models import new
from data.models import Solo1

def about(request):
    return HttpResponse("<h1>HEY THERE! THIS IS RUDRANSH</h1>")
def aboutnext(request,abouttid):
    return HttpResponse(abouttid)
def HOME(request):
    print(request.headers['content_type'])
    servicesData=Solo.objects.all() 
    data={
        'servicesData':servicesData
        }
    if request.method=="POST":
         email1=request.POST.get('num')
         enn=Solo1(email=email1)
         enn.save()
    return render(request,"index.html",data) 
def SIGN(request):
    return HttpResponse("sign")
def HOME1(request):
 try:
     if request.method=="POST":
         email4=(request.POST.get('num3'))
         pass4=(request.POST.get('num4'))
     if (request.POST['num3'])=="":
             return render(request,"index1.html",{'error':True}) 
     enn=new(first=email4,second=pass4)
     enn.save()
     return HttpResponseRedirect('/Signed-in/')
 except:
     pass
     return render(request,"index1.html")
def THANK(request):
    return render(request,"thank.html")

   
