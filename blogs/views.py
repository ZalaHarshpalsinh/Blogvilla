from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Blog,User
from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    pass

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return HttpResponseRedirect(reverse('blogs:login'))
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {
            'form' : form,
        })
    else:
        return HttpResponseRedirect(reverse('blogs:index'))

def login_request(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('blogs:index'))
        else:
            form = AuthenticationForm()
        
        return render(request, 'login.html', {
            'form' : form,
        })
    else:
        return HttpResponseRedirect(reverse('blogs:index'))

def logout_request(request):
    pass
def myblogs(request):
    pass
def single_blog(request):
    pass
def update_blog(request):
    pass
def delete_blog(request):
    pass
