from django.urls import path
from . import views

urlpatterns=[
	path('', views.home, name='a1-home'),
	path('about/',views.about, name='a1-about'),
]
