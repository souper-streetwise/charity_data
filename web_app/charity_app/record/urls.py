from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.record_create),
	path('<path:entry_method>/', views.record_create, name = "record_create"),
]