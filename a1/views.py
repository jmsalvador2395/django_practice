from django.shortcuts import render
from django.http import HttpResponse

dummy_posts=[
	{
		'author':'john',
		'title':'blog post 1',
		'content': 'hello',
		'date_posted':'May 8, 2018'
	},
	{
		'author':'jane',
		'title':'blog post 2',
		'content':'hi',
		'date_posted':'May 9, 2019'
	}
]
def home(request):
	context = {
		'posts':dummy_posts
	}
	return render(request, 'a1/home.html', context)

def about(request):
	return render(request, 'a1/about.html',{'title': 'about'})
