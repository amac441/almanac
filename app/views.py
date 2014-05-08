# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app.models import Signup, SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form':form,
    })
