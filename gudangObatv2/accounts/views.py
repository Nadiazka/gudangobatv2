from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import transaction
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@transaction.atomic
def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			print("Form Valid")
			user = form.save()
			profile.user = user
			profile.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Selamat '+ username +', akun kamu berhasil dibuat')
			return redirect('login')
		else:
			print("Form tidak valid")
	else:
		form = CreateUserForm()
		print("tidak ada request POST")

	context = {
	'form' : form
	}
	return render (request, 'accounts/register.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('$')
		else:
			messages.info(request, 'Username atau Password salah')

	return render (request, 'accounts/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')