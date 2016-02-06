from django.conf.urls import url, patterns
from django.contrib import admin

urlpatterns = [
   	url(r'^$', 'timeismoney.views.home', name='home'),
    url(r'^createEvent$', 'timeismoney.views.createEvent', name='createEvent'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'timeismoney/login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register$', 'timeismoney.views.register', name='register'),
]
