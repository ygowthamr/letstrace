from django.urls import path
from . import views

urlpatterns = [
	path('main',views.main,name="main"),
	path('results', views.results, name="results"),
]
