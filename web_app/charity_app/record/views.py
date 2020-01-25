from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
	title = "Streetwise"
	#return HttpResponse(title)
	return render(request, 'base.html', {'title': title})


# Create your views here.
