from django.shortcuts import render
from myapp.models import BlogApp

def BlogView(request):

    blog = BlogApp.objects.all()

    return render(request,'myapp/index.html',{'Nilesh':blog})