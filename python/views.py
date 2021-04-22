from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryView(request, cats):
	cat_posts = Post.objects.filter(category__iexact=cats.replace('-', ' ').replace('roj','RÓJ'))
	context = {}
	context['cats'] = cats.title().replace('-', ' ').replace('roj','rój')
	context['cat_posts'] = cat_posts
	cat_menu = Category.objects.all()
	context["cat_menu"] = cat_menu
	return render(request, 'categories.html', context)
	#{'cats': cats.title().replace('-', ' ').replace('roj','rój'), 'cat_posts': cat_posts}

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = ('title','title_tag','body')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'edit_post.html'
	#fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

def aboutme(request):
	return render(request, 'aboutme.html', {})

def contact(request):
	return render(request, 'contact.html', {})