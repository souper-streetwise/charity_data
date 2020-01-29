from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         print("True You can redirect.")
#         # Redirect to a success page.
#     else:
#         print("Wrong information")
#         #invalid
#         pass

        
# def logout(request):
#     logout(request)
#     # Redirect to a success page.