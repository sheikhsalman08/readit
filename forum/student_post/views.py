from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Post
from .models import Student

# Create your views here.

def list_posts(request):

	posts = Post.objects.exclude(date_posted__isnull = True)

	context = {
		'posts' : posts,
	}

	return render(request,"list.html",context)

class Students_list(View):
	def get(self, request):

		students = Student.objects.all()

		context = {
			'students': students
		}

		return render(request,"students.html",context)

class Post_details(DetailView):
	model = Post
	template_name = 'post_details.html'