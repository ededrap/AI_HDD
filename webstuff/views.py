from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import HeartForm

# Create your views here.
def index(request):
	return render(request, 'index.html', {'form': HeartForm})

def calculate(request):
	print(request.data)
	return '1'
