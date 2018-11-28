from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time

from .forms import HeartForm

# Create your views here.
def index(request):
	return render(request, 'index.html', {'form': HeartForm})

@csrf_exempt
def calculate(request):
	print(request.POST['attribute1'])
	data = request
	time.sleep(2)
	return JsonResponse({'result' : '1', 'accuracy': '100%'})