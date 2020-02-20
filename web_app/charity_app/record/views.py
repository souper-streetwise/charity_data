from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RecordForm
from django.contrib import messages
#from django.shortcuts import redirect

# @login_required
# def homepage(request):
# 	title = "This my Records Page"
# 	return render(request, 'homepage.html', {'title': title})

@login_required
def record_create(request):
	form = RecordForm(request.POST or None)

	if request.POST:
		print("Item submitted")
		form.save()

	if form.is_valid():
		messages.success(request, 'Form submission successful')


	return render(request,"record/add_item.html",{'title':"Record Item","form": form})



# def redirect_view(request):
#     response = redirect('/redirect-success/')
#     return response


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