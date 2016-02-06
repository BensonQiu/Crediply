# from timeismoney.forms import RegistrationForm
from timeismoney.models import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

@login_required
def createEvent(request):
	context = {}
	return render(request, 'timeismoney/createEvent.html', context)

@login_required
def home(request):
	context = {}
	return render(request, 'timeismoney/index.html', context)

#@transaction.atomic
def register(request):

	# If this is a GET request, display the registration form.
	if request.method == 'GET':
		return render(request, 'timeismoney/register.html', {})

	# TODO: Create a form to validate input
	form = request.POST
	# TODO: Do form validation here.
	new_user = User.objects.create_user(
		username=form['username'],
		password=form['password1'],
		first_name=form['first_name'],
		last_name=form['last_name'],
		email=form['email'],
	)

	# import ipdb; ipdb.set_trace()
	return render(request, 'timeismoney/login.html', {})
