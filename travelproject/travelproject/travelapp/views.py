from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import People

# Create your views here.
def demo(request):
   obj=Place.objects.all()
   obj1=People.objects.all()

   return render(request,"index.html",{'result':obj,'result1':obj1})








# def about(request):
#    return render(request,"about.html)
# def contact(request):
#    return HttpResponse("hello im contact")
# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    return render(request,"result.html",{'result':res})