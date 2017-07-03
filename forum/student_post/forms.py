from django import forms
from .models import Post

class PostForm(forms.Form):

	title = forms.CharField(
		widget = forms.Textarea,
		min_length= 1,
		error_messages={
			'required': 'Please enter your review',
			'min_length': 'Please write at least 300 characters'
		}
	)

	post = forms.CharField(
		widget = forms.Textarea,
		min_length= 1,
		error_messages={
			'required': 'Please enter your review',
			'min_length': 'Please write at least 300 characters'
		}
	)

class PostFormClassBassed(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'post','post_owner']