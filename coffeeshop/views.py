from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        'home' : True
    }
    return render(request, 'homepage/index.html', context)

def about(request):
    context = {
        'about' : True
    }
    return render(request, 'homepage/about.html', context)

def menu(request):
    context = {
        'menu' : True
    }
    return render(request, 'homepage/menu.html', context)