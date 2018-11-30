from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from webstuff.hddmlformula import train, ask
from webstuff.preprocessor import gather_data

from .forms import HeartForm


def index(request):
	return render(request, 'index.html', {'form': HeartForm})


@csrf_exempt
def calculate(request):
	query = request.POST['age'] + "," + request.POST['sex'] + "," + request.POST['cp'] + "," + request.POST['trestbps'] + "," + request.POST['chol'] + "," + request.POST['fbs'] + "," + request.POST['restecg'] + "," + request.POST['thalach'] + "," + request.POST['exang'] + "," + request.POST['oldpeak'] + "," + request.POST['slope'] + "," + request.POST['ca'] + "," + request.POST['thal']
	name = request.POST['name']
	age = float(request.POST['age'])
	sex = float(request.POST['sex'])
	cp = float(request.POST['cp'])
	trestbps = float(request.POST['trestbps'])
	chol = float(request.POST['chol'])
	fbs = float(request.POST['fbs'])
	restecg = float(request.POST['restecg'])
	thalach = float(request.POST['thalach'])
	exang = float(request.POST['exang'])
	oldpeak = float(request.POST['oldpeak'])
	slope = float(request.POST['slope'])
	ca = float(request.POST['ca'])
	thal = float(request.POST['thal'])

	if 'dataset' not in request.session:
		dataset = gather_data()
		request.session['dataset'] = dataset
	else:
		dataset = request.session['dataset']

	if 'tree' not in request.session:
		training = train(dataset)
		tree = training[0]
		accuracy = training[1]
		request.session['tree'] = tree
		request.session['accu'] = accuracy
	else:
		tree = request.session['tree']
		accuracy = request.session['accu']
	request.session.set_expiry(60)  # Tree data Expires in 1 minute

	result = ask(query, tree)

	return JsonResponse({'name': name, 'result': result, 'accuracy': accuracy})
