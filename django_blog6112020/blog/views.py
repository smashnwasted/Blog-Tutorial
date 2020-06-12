from django.shortcuts import render
from django.http import HttpResponse



# Logic for how we handel certain routes
posts = [
			{
			'author': 'Ryan',
			'title': 'Ryan posts',
			'content': 'Ryans first post',			
			'date_posted': 'today'
			},

			{
			'author': 'Ryan',
			'title': 'Ryan posts',
			'content': 'Ryans second post',			
			'date_posted': 'today'
			}
]


def home(request):
	return render(request, 'blog/home.html')

def about(request):
	return render(request, 'blog/about.html')