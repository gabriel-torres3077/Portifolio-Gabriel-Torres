from multiprocessing import context
from django.shortcuts import render
from .models import Gabriel

# Create your views here.
def index(request):
    #gabriel object
    gabriel = Gabriel.objects.latest('updated')

    context = {
        'gabriel': gabriel,
    }
    return render(request, 'index.html', context)
