from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Meeting(models.Model):
	meetingName = models.CharField(max_length=100)
	dateAndTime = models.DateTimeField()
	location = models.CharField(max_length=100)
	attendees = models.CharField(max_length=200)
	# acceptStatus = models.BooleanField()
