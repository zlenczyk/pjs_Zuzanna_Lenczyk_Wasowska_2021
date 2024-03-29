from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('post-detail', args=(str(self.id)))
		return reverse('home')

		

class Tag(models.Model):
	namee = models.CharField(max_length=255)

	def __str__(self):
		return self.namee

	def get_absolute_url(self):
		#return reverse('post-detail', args=(str(self.id)))
		return reverse('home')


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	nickname = models.TextField(max_length=255, null = True, blank=True)
	instagram = models.CharField(max_length=255, null = True, blank=True)
	pinterest = models.CharField(max_length=255, null = True, blank=True)
	profile_pic = models.ImageField(null = True, blank=True, upload_to="images/profile/" )

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null = True, blank=True, upload_to="images/" )
	title_tag = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	#body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=255, default='brak kategorii' )
	tag = models.CharField(max_length=255, default='brak tagu')

	class Meta:
		ordering = ['-id']


	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('post-detail', args=(str(self.id)))
		return reverse('home')


