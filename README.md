# TimeIsMoney

TimeisMoney is a web application designed to gamify the act of arriving on time. Users can set up meetings on our web app and check in to their location when they arrive. Users who do not check in on time are charged a fee using Nessie, Capital One's Hackathon API.

TimeIsMoney was built in 24 hours for TartanHacks 2016. 

## Usage Instructions

```
$ virtualenv venv
```

```
$ source venv/bin/activate
```

```
$ pip install -r requirements.txt
```

```
$ cd mysite; python manage.py makemigrations; python manage.py migrate; python manage.py runserver
```
