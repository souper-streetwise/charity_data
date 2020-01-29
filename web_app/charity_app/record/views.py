from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RecordForm

@login_required
def homepage(request):
	title = "This my Records Page"
	return render(request, 'homepage.html', {'title': title})

@login_required
def record_create(request):
	form = RecordForm(request.POST or None)

	if request.POST:
		print("You create instance")
		form.save()


	return render(request,"record/add_item.html",{'title':"Create Record","form": form})