# Create your views here.

from django.http import HttpResponse
from ads.models import Authentication

def index(request):
	return HttpResponse("Hello, world. Index Page.")

def display(request,ad_id):
	return HttpResponse("Message of Ad %s is being displayed." % ad_id)

def authenticate(request):
	if request.method == "GET":
		pi_name	= request.GET.get('pi_name','')
		uniq_id	= request.GET.get('uniq_id','')
		Authentications = Authentication.objects.all()
		for auth in Authentications:
			if pi_name == auth.pi_name \
			and uniq_id == auth.uniq_id:
				# Check if Pi is in use
				if auth.in_use == False:
					return HttpResponse("OK!")
				else:
					return HttpResponse("Sign is currently in use. Please try again later.")
	# Fallback respone
	return HttpResponse("Something went wrong! Please re-scan the QR code!")
