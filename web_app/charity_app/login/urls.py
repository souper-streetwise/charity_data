from django.urls import path

from login import views

urlpatterns = [
    path('', views.logout_request, name='logout')
]