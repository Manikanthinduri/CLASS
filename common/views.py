from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('class.html')
    return HttpResponse(template.render())


def registration(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
