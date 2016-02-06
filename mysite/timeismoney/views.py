import datetime

from timeismoney.models import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect

@login_required
def createMeeting(request):
	context = {}

	if request.method == 'GET':
		return render(request, 'timeismoney/createMeeting.html', context)

	# TODO: Create a form to validate input
	form = request.POST

	newMeeting = Meeting(
		meetingName=form['meetingName'],
		dateAndTime=datetime.datetime.utcnow(), # TODO: Get date and time from form.
		location=form['location'],
		attendees=form['attendees'],
	)
	newMeeting.save()

	return redirect(reverse('home'))

@login_required
def home(request):
	context = {}
	context['meetings'] = Meeting.objects.all()

	return render(request, 'timeismoney/index.html', context)

@transaction.atomic
def register(request):

	# If this is a GET request, display the registration form.
	if request.method == 'GET':
		return render(request, 'timeismoney/register.html', {})

	# TODO: Create a form to validate input
	form = request.POST
	# TODO: Do form validation here.
	newUser = User.objects.create_user(
		username=form['username'],
		password=form['password1'],
		first_name=form['first_name'],
		last_name=form['last_name'],
		email=form['email'],
	)

	return render(request, 'timeismoney/login.html', {})
