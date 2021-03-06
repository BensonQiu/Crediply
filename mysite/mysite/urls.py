import datetime
import json
import pytz
import requests
import threading
import time

from django.conf.urls import url, patterns
from django.contrib import admin

from timeismoney.models import *

urlpatterns = [
    url(r'^$', 'timeismoney.views.home', name='home'),
    url(r'^attend(?P<id>[0-9_-]+)$', 'timeismoney.views.attend', name='attend'),
    url(r'^createMeeting$', 'timeismoney.views.createMeeting', name='createMeeting'),
    url(r'^checkIn$', 'timeismoney.views.checkIn', name='checkIn'),
    url(r'^summary(?P<meetingName>.*)$', 'timeismoney.views.summary', name='summary'),
    url(r'^getData$', 'timeismoney.views.getData'),
    url(r'^getUsernames$', 'timeismoney.views.getUsernames'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'timeismoney/login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register$', 'timeismoney.views.register', name='register'),
]

def hasStarted(startDT):
    startYear = int(startDT[0:4])
    startMonth = int(startDT[5].strip('0') + startDT[6])
    startDay = int(startDT[8].strip('0') + startDT[9])
    startHour = int(startDT[10].strip('0') + startDT[11])
    startMinute = int(startDT[13].strip('0') + startDT[14])

    gmt = pytz.timezone('GMT')
    eastern = pytz.timezone('US/Eastern')
    dategmt = gmt.localize(datetime.datetime.now())
    currDT = dategmt.astimezone(eastern)
    currYear = currDT.year
    currMonth = currDT.month
    currDay = currDT.day
    currHour = currDT.time().hour
    currMinute = currDT.time().minute

    return currYear >= startYear and currMonth >= startMonth and currDay >= startDay and \
           ((currHour > startHour) or (currHour == startHour and currMinute >= startMinute))

def transfer_balance(payer_id='56241a14de4bf40b17112ece',
        payee_id='56241a14de4bf40b17112ece', amount=1,
        api_key='9796d298ca02479fd5b384a8afe6d20e'):
    base_url = 'http://api.reimaginebanking.com/accounts/{_id}/transfers?key={api_key}'
    url = base_url.format(
        _id=payer_id,
        api_key=api_key,
    )
    headers = {'content-type': 'application/json'}
    payload = {
        'medium': 'balance',
        'payee_id': payee_id,
        'amount': amount,
        'status': 'pending',
        'description': 'A transfer balance for being late to a meeting',
    }
    payload = json.dumps(payload)
    response = requests.post(url, data=payload, headers=headers)

    # print 'Made a transfer balance with response={response}'.format(response=response)
    # print response.text
    print 'Made a payment of ${amount}'.format(amount=amount)


def checkLateAttendees(x=1):
    while True:
        transfer_balance()
        x += 1
        print("Counter:{x}".format(x=x))
        for meeting in Meeting.objects.all():
            # Meeting has not been accepted by everyone yet
            if meeting.pendingAttendees.all():
                print('Skipping {meetingName}'.format(meetingName=meeting.meetingName))
                continue
            # Meeting hasn't started yet
            if not hasStarted(meeting.startDT):
                print('Meeting {meetingName} not started'.format(meetingName=meeting.meetingName))
                continue
            checkedinAttendees = meeting.checkedinAttendees.all()
            for attendee in meeting.acceptedAttendees.all():
                if attendee not in checkedinAttendees:
                    print('{username} is late for {meetingName}'.format(
                        username=attendee.username,
                        meetingName=meeting.meetingName,
                    ))

        time.sleep(2)

t = threading.Thread(target=checkLateAttendees,
                     kwargs={'x': 5})
t.setDaemon(True)
# t.start()
