from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 

def old_add2_redirect(request,a,b):
	return HttpResponseRedirect(
		reverse('add2',args=(a,b))
	)
	#new4

def index(request):
	return render(request,'home.html')
	#new3

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(str(c))
	#new1

def add2(request,a,b):
	c = int(a)+int(b)
	return HttpResponse(str(c))
	# number is 'int', add have restrict
	#new2
	
