from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Home,Profile,Portfolio,Category,Skills

# Create your views here.
def home(request):
    #Home
    home=Home.objects.latest('updated_time')
    #About
    about=About.objects.latest('updated_time')
    profiles=Profile.objects.filter(about=about)
    #skills
    categories=Category.objects.all()
    #portfolio
    portfolios=Portfolio.objects.all()

    context={
        'home':home,
        'profiles':profiles,
        'about':about,
        'categories':categories, 
        'portfolios':portfolios, 
    }
    return render(request, 'index.html',context)