from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from webstuff.hddmlformula import main
import time

from .forms import HeartForm

# Create your views here.
def index(request):
	return render(request, 'index.html', {'form': HeartForm})

@csrf_exempt
def calculate(request):
	data = request.POST['age'] + "," + request.POST['sex'] + "," + request.POST['cp'] + "," + request.POST['trestbps'] + "," + request.POST['chol'] + "," + request.POST['fbs'] + "," + request.POST['restecg'] + "," + request.POST['thalach'] + "," + request.POST['exang'] + "," + request.POST['oldpeak'] + "," + request.POST['slope'] + "," + request.POST['ca'] + "," + request.POST['thal']
	print(data)
	name = request.POST['name']
	age = float(request.POST['age'])
	sex = float(request.POST['sex'] )
	cp  = float(request.POST['cp'])
	trestbps = float(request.POST['trestbps'] )
	chol = float(request.POST['chol'] )
	fbs = float(request.POST['fbs'] )
	restecg =  float(request.POST['restecg'] )
	thalach = float(request.POST['thalach'] )
	exang =  float(request.POST['exang'] )
	oldpeak  = float(request.POST['oldpeak'] )
	slope = float(request.POST['slope'])
	ca = float(request.POST['ca'])
	thal  =  float(request.POST['thal'])
	
	result = main(data)
	
	
	return JsonResponse({'result' : result[1], 'accuracy': result[0]})
