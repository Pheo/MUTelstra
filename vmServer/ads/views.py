# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. Index Page.")

def detail(request, ad_id):
	return HttpResponse("You're looking at Advertisment %s." % ad_id)
