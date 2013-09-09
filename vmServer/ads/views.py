# Create your views here.

from django.http import HttpResponse
from ads.models import Authentication

def index(request):
	return HttpResponse("Hello, world. Index Page.")

def display(request,ad_id):
	return HttpResponse("Message of Ad %s is being displayed." % ad_id)

# Authenticate is run when requesting permission to use Sign
def authenticate(request):
	if request.method == "GET":
		get_pi_name = request.GET.get('pi_name','')
		get_uniq_id = request.GET.get('uniq_id','')
		# Log into sign 
		query = Authentication.objects.filter(pi_name=get_pi_name, uniq_id=get_uniq_id, in_use=False).update(in_use=True)
		if query == 1:
			return HttpResponse('<meta http-equiv="refresh" content="2; url=http://203.42.134.228/">\
				Successfully signed into sign! Redirecting now.')
		else:
			return HttpResponse("Sign is currently in use. Please try again later.")
	# Fallback response
	return HttpResponse("Something went wrong! Please re-scan the QR code!")

# Session is run when sign has to notify VM when the Sign is no longer in use.
def session(request):
	if request.method == "GET":
		get_pi_name = request.GET.get('pi_name','')
		get_uniq_id = request.GET.get('uniq_id','')
		# Log out of sign
		query = Authentication.objects.filter(pi_name=get_pi_name, uniq_id=get_uniq_id, in_use=True).update(in_use=False)
		# Do something that tells sign to display 'Thanks for playing'
		if query == 1:
			return HttpResponse("Thank you for playing!")
		else:
			return HttpResponse("Sign currently not in use. There is no need to log out!")

	# Fallback response
	return HttpResponse("Unable to log out of sign. Please try again later!")
