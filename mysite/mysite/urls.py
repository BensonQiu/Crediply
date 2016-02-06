from django.conf.urls import url, patterns
from django.contrib import admin

urlpatterns = [
   	url(r'^$', 'timeismoney.views.home', name='home'),
    url(r'^createMeeting$', 'timeismoney.views.createMeeting', name='createMeeting'),
    url(r'^checkIn$', 'timeismoney.views.checkIn', name='checkIn'),
    url(r'^getData$', 'timeismoney.views.getData'),
    url(r'^getUsernames$', 'timeismoney.views.getUsernames'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'timeismoney/login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register$', 'timeismoney.views.register', name='register'),
]
