from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.
def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			if usuario.is_active:
				login(request, usuario)
				return HttpResponseRedirect(reverse('actas:mesa_municipal'))				
			else:
				return HttpResponseRedirect(reverse('usuarios:login'))				
		else:
			return HttpResponseRedirect(reverse('usuarios:login'))
	else:
		return render(request, 'usuarios/login.html')

