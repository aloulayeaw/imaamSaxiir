from django.shortcuts import render

# Create your views here.

def homeindex(request):
    
    return render(request, 'base/index.html')

def tafsir(request):
    
    return render(request, 'base/tafsir.html')

def about(request):
    
    return render(request, 'base/about.html')

def publications(request):
    
    return render(request, 'base/publications.html')

def gallery(request):
    
    return render(request, 'base/gallery.html')


def poeme(request):
    
    return render(request, 'base/poeme.html')
