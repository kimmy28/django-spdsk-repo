from django.shortcuts import render
from django.http import HttpResponse

def banksampah_login_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='banksampah').exists():
             return function(request, *args, **kwargs)
        else:
             return HttpResponse('/wasteweb/error/', context_instance=RequestContext(request))

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def operator_login_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='operator').exists():
             return function(request, *args, **kwargs)
        else:
             return HttpResponse('/wasteweb/error/', context_instance=RequestContext(request))

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
