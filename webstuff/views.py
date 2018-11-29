from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import HeartForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {'form': HeartForm})

def calculate(request):
    return JsonResponse({
        'sebuahtest':"kekeke"
    })
