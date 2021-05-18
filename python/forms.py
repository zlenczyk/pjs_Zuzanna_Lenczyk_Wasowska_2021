from django import forms
from .models import Post, Category, Tag

choice_list = []
choices = Category.objects.all().values_list('name','name')
for item in choices:
    choice_list.append(item)

tag_list = []
tags = Tag.objects.all().values_list('namee','namee')
for it in tags:
    tag_list.append(it)

class PostForm(forms.ModelForm):

    class Meta:
        '''def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            choices = Category.objects.all().values_list('name','name')
            for item in choices:
                choice_list.append(item)
            self.fields['category'].choices = choice_list

            tags = Tag.objects.all().values_list('namee','namee')
            for it in tags:
                tag_list.append(it)
            self.fields['tag'].tags = tag_list'''
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'tag', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'tag': forms.Select(choices=tag_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }