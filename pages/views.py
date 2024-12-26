from django.shortcuts import render
from django.http import HttpResponse
from .models import Flower

# Create your views here.


def index(request):

    flowers = Flower.objects.all()

    context = {
        'flowers' : flowers,
    }

    return render(request, 'pages/index.html', context)