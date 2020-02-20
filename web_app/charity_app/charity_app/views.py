from django.contrib.auth import logout
from django.http import HttpResponse


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return HttpResponse("<h1>Logged out</h1>")
    # Redirect to a success page.