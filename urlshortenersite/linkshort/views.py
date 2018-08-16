from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
import random, requests
from .models import Link

def index(request):
	short_url = None
	if request.method == 'POST':
		uncoded = request.POST['url_input']
		if Link.objects.filter(url=uncoded).exists():
			existing = Link.objects.get(url=uncoded)
			short_url = existing.shortened
		else:		
			short_url = shorten_url(uncoded)
			new_url = Link(url=uncoded, shortened=short_url)
			new_url.save()
	links = Link.objects.all()
	context = {
		'shortened': short_url,
		'urls' : links,
	}
	return render(request, 'linkshort/index.html', context)


def shorten_redirect(request, shortened):
	link = get_object_or_404(Link, shortened=shortened)
	return redirect(link.url)


	# return HttpResponse(shortene

def shorten_url(long_url):
	while True:
		choices = '12345567890qwertyuiopasdfghjklzxcvbnm'
		shorten_url = ''.join([random.choice(choices) for i in range(7)])
		if not Link.objects.filter(shortened=shorten_url).exists():
			return shorten_url
#link out the lenghtened url between a thing