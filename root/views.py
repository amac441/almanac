from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.models import User
from years.models import UserProfile, Signup
from years.forms import UserCreateForm, ProfileForm, SignupForm, ProblemForm

from django.template import RequestContext


def signup(request):
    if request.method == 'POST':
        sform = SignupForm(request.POST, instance=Signup())
        pform = ProblemForm(request.POST, instance=Signup())
        if sform.is_valid() and pform.is_valid():
            sform.save()
            pform.save()
            return redirect('/thanks')

    else:
        sform = SignupForm()
        pform = ProblemForm()

    return render(request, 'logins/signup.html', {'sform':sform, 'pform':pform})


def login(request):
	c={}
	c.update(csrf(request))

	form = AuthenticationForm

	return render(request, 'logins/login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)  #set state or auth object
		return HttpResponseRedirect('/years')  #change this to some other site
	else:
		return HttpResponseRedirect('/invalid')

def loggedin(request):
	return render_to_response('/years', {'full_name':request.user.username})

def invalid_login(request):
	return render_to_response('logins/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('index.html')

def register_user(request):
	#http://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/
    if request.method == "POST":
        uform = UserCreateForm(request.POST, instance=User())
        pforms = [ProfileForm(request.POST, prefix=str(x), instance=UserProfile()) for x in range(0,2)]
        if uform.is_valid() and all([cf.is_valid() for cf in pforms]):
            new_user = uform.save()
            for cf in pforms:
                new_profile = cf.save(commit=False)
                new_profile.user = new_user
                new_profile.save()
            return HttpResponseRedirect('/5years')
    else:
        uform = UserCreateForm(instance=User())
        pforms = [ProfileForm(prefix=str(x), instance=UserProfile()) for x in range(0,2)]
        pforms = ProfileForm()
    return render_to_response('logins/register.html', {'user_form': uform, 'profile_forms': pforms}, RequestContext(request))
