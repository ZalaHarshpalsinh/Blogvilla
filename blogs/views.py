from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Blog,User
from .forms import UserCreationForm, AuthenticationForm, BlogForm

# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {
        'blogs' : blogs,
    })

@login_required
def single_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog_visit.html', {
        'blog' : blog,
    })

def register(request):
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

@login_required
def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogs:login'))

@login_required
def myblogs(request):
    my_blogs = Blog.objects.filter(user=request.user)
    blog_form = BlogForm()
    return render(request, 'my_blogs.html', {
        'my_blogs' : my_blogs,
        'blog_form' : blog_form,
    })

@login_required
def update_blog(request):
    pass

@login_required
def delete_blog(request):
    pass
