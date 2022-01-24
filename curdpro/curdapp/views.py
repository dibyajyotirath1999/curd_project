from audioop import add
from django.shortcuts import render,redirect
from .models import adddatamod

def displaydata(request):
    studentdata=adddatamod.objects.all()


    return render(request,"display.html",{"students":studentdata,})


def adddata(request):
    if request.method== "POST":
        adddatamod(
         fname=request.POST.get("fname"),
         lname=request.POST.get("lname"),
         course= request.POST.get("course"),
         fee=request.POST.get("fee"),
         assignment1=request.POST.get("a1"),
         assignment2=request.POST.get("a2"),
         assignment3=request.POST.get("a3"),
         assignment4=request.POST.get("a4"),
         total =int(request.POST.get("a1"))+int(request.POST.get("a2"))+int(request.POST.get("a3"))+int(request.POST.get("a4")),
         avg= (int(request.POST.get("a1"))+int(request.POST.get("a2"))+int(request.POST.get("a3"))+int(request.POST.get("a4")))/4

        ).save()
        return redirect("displaydata")
    else:
        return render (request,"adddata.html")

def update_data(request,id):
    if request.method=="POST":
        student = adddatamod.objects.get(id=id)
        student.fname=request.POST.get("fname")
        student.lname=request.POST.get("lname")
        student.course=request.POST.get("course")
        student.fee=request.POST.get("fee")
        student.assignment1= request.POST.get("a1")
        student.assignment2= request.POST.get("a2")
        student.assignment3= request.POST.get("a3")
        student.assignment4= request.POST.get("a4")
        student.total =int(request.POST.get("a1"))+int(request.POST.get("a2"))+int(request.POST.get("a3"))+int(request.POST.get("a4"))
        student.save()
        return redirect("displaydata")


    else:
        student = adddatamod.objects.get(id=id)
        return render(request,"update_data.html",{"student":student})


def delete_data(request,id):
    student = adddatamod.objects.get(id=id)
    student.delete()
    return redirect("displaydata")



