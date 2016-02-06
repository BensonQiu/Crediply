from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Meeting(models.Model):
	meetingName = models.CharField(max_length=100)
	dateAndTime = models.DateTimeField()
	location = models.CharField(max_length=100)
	pendingAttendees = models.ManyToManyField(User, related_name='%(class)s_pending')
	acceptedAttendees = models.ManyToManyField(User, related_name='%(class)s_accepted')

	def natural_key(self):
		return (self.pendingAttendees, self.acceptedAttendees)

