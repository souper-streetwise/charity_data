from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

from .forms import RecordForm


# @login_required
# def homepage(request):
# 	title = "This my Records Page"
# 	return render(request, 'homepage.html', {'title': title})


@login_required
def record_create(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.instance.charity = request.user.username
            form.save()
            messages.success(request, "Record saved successfully")
            return redirect("record_create")
    else:
        form = RecordForm()

    return render(
        request,
        "record/add_item.html",
        {"title": "Record Item", "form": form},
    )
