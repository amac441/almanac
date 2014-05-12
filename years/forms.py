# forms.py for authantication

from django import forms
from django.contrib.auth.models import User
from years.models import UserProfile, Signup
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1") #took out password2
        exclude = ('password2',)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        exclude = ('problem',)

class ProblemForm(forms.ModelForm):
    class Meta:
        model=Signup
        exclude = ('name','email','age','position')