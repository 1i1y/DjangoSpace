# coding: utf-8 
from django.shortcuts import render

# test2 --
def home(request):
    list = ["HTML", "CSS","jQuery","Python"]
    return render(request, 'home.html', {'list': list})
	
'''
test1 --
def home(request):
    string = u"這行是Django的語法"
    return render(request, 'home.html', {'string': string})
	
home.html:	
{{ string }}

test2 --
def home(request):
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})
'''
