from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
		try:
			form.save()
		except ValueError as err:
			messages.error(request, err)
			return render(request, "record/add_item.html", {'title': "Record Item", "form": form})

		messages.success(request,"Record saved successfully")
		return redirect("/")


	return render(request,"record/add_item.html",{'title':"Record Item","form": form})

# @login_required
# def record_create(request):
# 	submitted = False
# 	if request.method == 'POST':
# 		form = RecordForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/add_item/?submitted=True')
# 		else:
# 			form = VenueForm()
# 			if 'submitted' in request.GET:
# 				submitted = True
# 	return render(request, 'record/add_item.html', {'form': form, 'submitted': submitted})