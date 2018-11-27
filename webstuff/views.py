from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import HeartForm

# Create your views here.
def index(request):
    return HttpResponse("Greetings.")

def get_name(request):
    if request.method == 'POST':
        form = HeartForm(request.POST)
        if form.is_valid():
        	print(form)
        	return HttpResponseRedirect('google.com')

    else:
        form = HeartForm()
    return render(request, 'index.html', {'form':form})
