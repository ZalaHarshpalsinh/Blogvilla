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
    blogs = reversed(Blog.objects.all())
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

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.user = request.user
            blog.save()
    else:
        blog_form = BlogForm()

    update_form = BlogForm()
    my_blogs = reversed(Blog.objects.filter(user=request.user))
    return render(request, 'my_blogs.html', {
        'my_blogs' : my_blogs,
        'blog_form' : blog_form,
        'update_form' : update_form,
    })

@login_required
def update_blog(request, blog_id):

    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id, user=request.user)
        form = BlogForm(request.POST, request.FILES , instance=blog)
        if form.is_valid():
            form.save()
            return redirect(reverse('blogs:myblogs') + f"#{blog.id}")
    return redirect('blogs:myblogs')

@login_required
def delete_blog(request, blog_id):
    if request.method == 'POST':
        next_blog = request.POST['next_blog']
        pre_blog = request.POST['pre_blog']
        blog = get_object_or_404(Blog, id=blog_id, user=request.user)
        blog.delete()
        if next_blog:
            return redirect(reverse('blogs:myblogs') + f"#{next_blog}")
        elif pre_blog:
            return redirect(reverse('blogs:myblogs') + f"#{pre_blog}")

    return redirect('blogs:myblogs')    
