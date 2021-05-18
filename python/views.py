from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Post, Category, Tag
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.mail import send_mail

class HomeView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'home.html'
    ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        tag_menu = Tag.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        paginator = Paginator(cat_menu, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        context["tag_menu"] = tag_menu
        context["cat_menu"] = pages
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

def TagView(request, tags):
    tag_posts = Post.objects.filter(tag__iexact=tags.replace('-', ' ').replace('roj','RÓJ'))
    context = {}
    context['tags'] = tags.title().replace('-', ' ').replace('roj','rój')
    context['tag_posts'] = tag_posts
    tag_menu = Tag.objects.all()
    context["tag_menu"] = tag_menu
    return render(request, 'tags.html', context)
    #{'cats': cats.title().replace('-', ' ').replace('roj','rój'), 'cat_posts': cat_posts}    '''

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        tag_menu = Tag.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["tag_menu"] = tag_menu
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

class BlogSearchView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains=query).order_by('-id')

def aboutme(request):
    return render(request, 'aboutme.html', {})

def contact(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']

        send_mail(
            name,
            message,
            email,
            ['zuzia.lenczyk@gmail.com'],
            )


        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})