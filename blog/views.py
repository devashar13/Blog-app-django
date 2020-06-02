from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
    {
        'author':'Dev',
        'title':'Blog',
        'content':'First Post',
        'date_posted':'August 27,2018',
    },
    {
        'author':'ashar',
        'title':'Blog 2',
        'content':'Seond Post',
        'date_posted':'August 27,2018',
    }
]
def home(request):
    context={
        'posts':posts 
    }
    return render(request,'blog/home.html',context )
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
