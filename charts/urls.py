from django.urls import path

from charts import views

urlpatterns = [
    path("", views.showCharts, name="show_charts")
]