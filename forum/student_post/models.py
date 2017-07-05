from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=30)
	post_owner = models.ManyToManyField("Student",related_name="posts")
	post  = models.TextField()
	date_posted = models.DateTimeField(blank=True,null=True)

	def __str__(self):
		return "{} by {}".format(self.title, self.list_post_owners())

	def list_post_owners(self):
		return ", ".join([student.name for student in self.post_owner.all()])
	
	def save(self, *args, **kwargs):
		if (self.date_posted is None):
			self.date_posted = now()

		super(Post, self).save(*args, **kwargs)


class Student(models.Model):
	name = models.CharField(max_length=80)
	assign_to_lecturer = models.ForeignKey(User, blank = True, null = True, related_name='students')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('students', kwargs={'pk',self.pk})