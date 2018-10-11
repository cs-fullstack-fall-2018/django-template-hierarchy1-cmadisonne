from django.shortcuts import render

from .models import Movies


def index(request):
    movies = Movies.objects.all()
    context = {'movies': movies}
    return render(request, 'movieApp/index.html', context)

def about(request):
    return render(request, 'movieApp/about.html')

def test(request):
    return render(request, 'movieApp/test.html')