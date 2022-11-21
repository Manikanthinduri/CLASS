from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http import request
from django.shortcuts import render


class Registrationform(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(Registrationform, self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class Loginform(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username doest not exists")
            if user.checkpassword(password):
                raise forms.ValidationError("incorrect password")
            return render(request, 'invalid.html')
