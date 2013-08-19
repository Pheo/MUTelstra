# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. Index Page.")

def display(request,ad_id):
	return HttpResponse("Message of Ad %s is being displayed." % ad_id)
