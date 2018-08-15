from django.http import HttpResponse
from django.shortcuts import render
# import import get_object_or_404
# import request/short 
from .models import Link

def index(request):
	links = Link.objects.all()
	context = {'urls' : links}

	return render(request, 'linkshort/index.html', context)

def shorten_redirect(request, shortened):
	return HttpResponse(shortened)
