from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import View, DetailView
from django.views.generic.edit import CreateView
from .models import Post , Student
from .forms import PostForm, PostFormClassBassed

# Create your views here.

def list_posts(request):

	posts = Post.objects.exclude(date_posted__isnull = True)

	context = {
		'posts' : posts,
	}

	return render(request,"list.html",context)

class Insert_post_ClassBassed(View):
	def get(self, request):
		posts = Post.objects.all()
		context = {
			'posts' : posts,
			'form'	: PostFormClassBassed,
		}

		return render(request, "Insert_post_ClassBassed.html", context)

	def post(self, request):
		form = PostFormClassBassed(request.POST)
		posts = Post.objects.all()

		if form.is_valid():
			form.save()
			return redirect('Insert_post_ClassBassed')

		context = {
			'form' : form,
			'books' : posts,
		}
		
		return render(request, "Insert_post_ClassBassed.html", context)

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



def insert_post(request, pk):

	post = get_object_or_404(Post, pk=pk)

	if request.method == 'POST':
		#process with form
		form = PostForm(request.POST)

		if form.is_valid():
			post.title = form.cleaned_data["title"]
			post.post = form.cleaned_data["post"]
			post.save()

			return redirect('home')


	else:
		form = PostForm

	context = {
		'post': post,
		'form': form,
	}

	return render(request, "insert_post.html", context)
 
class CreateStudent(CreateView):
 	model = Student
 	fields = ['name']
 	template_name = 'createStudentCreateView.html'

 	def get_success_url(self):
 		return reverse('createStudentCreateView')