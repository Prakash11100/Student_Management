from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import Admin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Student_db
from .form import Student_form
# Create your views here.

def Home(request):
    return render(request,"Home.html")

def Register(request):
    if request.method == 'POST':
        name=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User.objects.create_user(username=name,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            return redirect('Login')
    else:        
        form=Admin()
        return render(request,"Register.html",{'form':form})
@login_required
def Student_List(request):
    dbdata=Student_db.objects.all()
    if request.method == 'POST':
        form=Student_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            contact=form.cleaned_data['Contact']
            mail=form.cleaned_data['Mail']
            dbdata=Student_db(Name=name,Contact=contact,Mail=mail)
            dbdata.save()
            return redirect('Student_List')
    else:
        form=Student_form()
        if dbdata!='':
            return render(request,'Student.html',{'form':form,'dbdata':dbdata})
        else:
            return render(request,'Student.html',{'form':form})

def update(request,id):
    dbdata=Student_db.objects.get(id=id)
    if request.method == 'POST':
        form=Student_form(request.POST)
        if form.is_valid():
            dbdata.Name=form.cleaned_data['Name']
            dbdata.Contact=form.cleaned_data['Contact']
            dbdata.Mail=form.cleaned_data['Mail']            
            dbdata.save()
            return redirect('Student_List')
    else:
        form=Student_form(initial={'Name':dbdata.Name,'Contact':dbdata.Contact,'Mail':dbdata.Mail})
        return render(request,'Update.html',{'form':form,'dbdata':dbdata})

def Delete(request,id):
    dbdata=Student_db.objects.get(id=id)
    dbdata.delete()
    return redirect('Student_List')