from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Blog,User
from .forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index(request):
    pass

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return HttpResponseRedirect(reversed('blogs:login'))
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {
            'form' : form,
        })
    else:
        return HttpResponseRedirect(reversed('blogs:index'))

def login(request):
    pass
def logout(request):
    pass
def myblogs(request):
    pass
def single_blog(request):
    pass
def update_blog(request):
    pass
def delete_blog(request):
    pass
