from django import forms
from .models import Blog_Post, Products, Comments, NewsLetter


class Blog_PostForm(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['title', 'post', 'tags', 'images', 'video_link']


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'product_image', 'product_link']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'comment_body', 'blog_post']


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['newsletter_subscriber']

