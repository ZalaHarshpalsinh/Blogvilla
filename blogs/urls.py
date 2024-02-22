from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('myblogs', views.myblogs, name='myblogs'),
    path('blogs/<blog_id>', views.single_blog, name='single_blog'),
    path('myblogs/<blog_id>/update', views.update_blog, name='update_blog'),
    path('myblogs/<blog_id>/delete', views.delete_blog, name='delete_blog'),
]