import datetime
from faker import Faker
from django.shortcuts import render, redirect
from django.http import HttpResponse
from secondApp.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.
def index(request):
    return HttpResponse('<h1> My second app </h1>')

def help(request):
    help_dict = {'inject_here': 'HELP PAGE'}
    return render(request, 'secondApp/index.html', context=help_dict)

def show_access_records(request):
    acc_rec = AccessRecord.objects.order_by('date')
    ar_dict = {'access_records': acc_rec}
    return render(request, 'secondApp/accessRecords.html', context=ar_dict)

def show_form(request):
    print(request.method)
    form = forms.CommentForm()
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            print('Form Data')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['url'])
            print(form.cleaned_data['comment'])
    ar_dict = {'form': form}
    return render(request, 'secondApp/fillForm.html', context=ar_dict)

def add_Webpage(request):
    if request.method == 'POST':
        form = forms.add_webpage_form(request.POST)
        if form.is_valid():
            webpage = form.save()
            print('form input is valid for ModelForm')
            topic_name = form.cleaned_data['topic']
            name = form.cleaned_data['name']
            url = form.cleaned_data['url']
            acr = AccessRecord.objects.get_or_create(name=webpage, date=Faker().date())[0]
            acr.save()
        return redirect('../accessRecords/')
    else:
        form = forms.add_webpage_form()
        return render(request, 'secondApp/fillWebpageForm.html', context={'form': form})


def temp_inherit(request):
    return render(request, 'secondApp/template_inheritance.html')

def home(request):
    return render(request, 'secondApp/home_sec_app.html')

# code to start a repo
# git remote add origin git@github.com:somilg1312/learn_backend.git
# git branch -M main # creates a main and sets this as master branch
# git push -u origin main pushes to origin and sets local main to point to origin main