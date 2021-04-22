from django.urls import path
#from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/add', AddPostView.as_view(),name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('about-me', views.aboutme, name='aboutme'),
    path('contact', views.contact, name='contact'),
    path('category/<str:cats>', CategoryView, name='category'),
]