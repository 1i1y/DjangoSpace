# coding: utf-8
from django.shortcuts import render

def home(request):
	dict = {'site':u'Lily','content':u'所學的程式'}
	return render(request,'home.html',{'dict':dict})
