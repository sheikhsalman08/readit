from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=30)
	post_owner = models.ManyToManyField("Student",related_name="posts")
	post  = models.TextField()
	date_posted = models.DateTimeField()

	def __str__(self):
		return self.title

class Student(models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name