from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

post = [
    {
        'author' : 'CoreyMS',
        'title': 'Blog Post1',
        'content' : 'Du contenu',
        'date_posted': '27 juillet 2018'
    },
    {
        'author' : 'Max',
        'title': 'Blog Post3',
        'content' : 'Encore du contenu',
        'date_posted': '14 juillet 2018'
    }
    ]

def home(request):
    context = {
        'posts':post,
        'title':'titre personnalisé'
    }
    return render(request,'blog/home.html',context)
    #return HttpResponse('<h1>home</h1>')


def about(request):
    return render(request,'blog/about.html')