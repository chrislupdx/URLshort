from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {'foo': 'bar'}
	return render(request, 'linkshort/index.html', context)

def shorten_redirect(request, shortened):
	return HttpResponse(shortened)
