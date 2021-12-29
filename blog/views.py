import contextlib
from typing import ContextManager
from django import contrib
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from blog.models import ROlE, User, user_form
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import InputForm
from .forms import InputmodelForm

def check_email_withid(email,id):
    users = user_form.objects.all()
    for x in users:
        if x.email == email:
            if int(x.id) != int(id):
            
                return 1
    return 0

def check_email(email):
    users = user_form.objects.all()
    for x in users:
        if x.email == email:
                return 1
    return 0


def form_change(request):
        form = InputmodelForm(request.POST)
        if form.is_valid():
            if request.POST.get("change"):
                if (check_email_withid(form['email'].value(),request.POST['user_id']) == 1):
                    obj = user_form.objects.get(id = request.POST['user_id'])
                    form = InputmodelForm({'role':obj.role,'first_name':obj.first_name,'last_name':obj.last_name,'email':obj.email,'number':obj.number})
                    error = "same email"
                    context={
                        'user':obj,
                        'form':form,
                        'error':error,
                    }
                    return render(request,'blog/form_edit.html',context)

                user = user_form.objects.get(id=request.POST['user_id'])
                user.first_name = form['first_name'].value()
                user.last_name = form['last_name'].value()
                user.email = form['email'].value()
                user.number = form['number'].value()
                user.role = form['role'].value()
                user.save()

                users = user_form.objects.all()
                count = user_form.objects.all().count()
                context = {
                    'users':users,
                    'count':count
                }
                return render(request, 'blog/modelform_home.html',context)
            else:
                user = user_form.objects.get(id=request.POST['user_id'])
                user.delete()
                users = user_form.objects.all()
                count = user_form.objects.all().count()
                context = {
                    'users':users,
                    'count':count
                }
                return render(request, 'blog/modelform_home.html',context)

        else:
            obj = user_form.objects.get(id = request.POST['user_id'])
            form = InputmodelForm({'role':obj.role,'first_name':obj.first_name,'last_name':obj.last_name,'email':obj.email,'number':obj.number})
            error = "Please enter correct details"
            context={
                'user':obj,
                'form':form,
                'error':error,
            }
            return render(request,'blog/form_edit.html',context)
            




def form_edit(request,id):
    obj = user_form.objects.get(pk=id)
    form = InputmodelForm({'role':obj.role,'first_name':obj.first_name,'last_name':obj.last_name,'email':obj.email,'number':obj.number})
    context={
        'user':obj,
        'form':form
    }
    return render(request,'blog/form_edit.html',context)



def form(request):
    new_form = InputmodelForm()
    context={}
    context['form'] = new_form
    return render(request,'blog/form.html',context)

def new_register(request):
    form = InputmodelForm(request.POST)
    if form.is_valid():
        if (check_email(form['email'].value())):
            context={}
            new_form = InputmodelForm()
    
            context['form'] = new_form
            context['error'] = "same email"
            return render(request,'blog/form.html',context)
            

        form.save()
        users = user_form.objects.all()
        count = user_form.objects.all().count()
        context = {
                    'users':users,
                    'count':count
                }
        return render(request, 'blog/modelform_home.html',context)
    else:
        context={}
        new_form = InputmodelForm()
    
        context['form'] = new_form
        context['error'] = "Please enter correct details"
        return render(request,'blog/form.html',context)



def modelform(request):
    users = user_form.objects.all()
    count = user_form.objects.all().count()
    context = {
                'users':users,
                'count':count
            }

    return render(request,'blog/modelform_home.html',context)


