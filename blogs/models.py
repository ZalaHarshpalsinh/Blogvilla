from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Title:{self.title}\nContent:{self.content}\n"
