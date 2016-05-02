from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	name = str(request.GET.get('name'))
	if name == 'facebook':
		return HttpResponse('FB://profile')
	elif name == 'uber':
		return HttpResponse('Uber://')


