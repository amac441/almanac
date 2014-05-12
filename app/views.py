# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


#======== angular app.js call ================

def home(request, template_name="index.html"):
    return render_to_response(template_name,
                              context_instance=RequestContext(request))


#======== rest url definitions ===============