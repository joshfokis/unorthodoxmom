from django.contrib import admin
from django import forms
from .models import Blog_Post, Products, Comments, NewsLetter

class Blog_PostAdminForm(forms.ModelForm):

    class Meta:
        model = Blog_Post
        fields = '__all__'


class Blog_PostAdmin(admin.ModelAdmin):
    form = Blog_PostAdminForm
    list_display = ['title', 'slug', 'created', 'last_updated', 'post', 'tags', 'images', 'video_link']
    # readonly_fields = ['title', 'slug', 'created', 'last_updated', 'post', 'tags', 'images', 'video_link']

admin.site.register(Blog_Post, Blog_PostAdmin)


class ProductsAdminForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'


class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'product_image', 'product_link']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'product_image', 'product_link']

admin.site.register(Products, ProductsAdmin)


class CommentsAdminForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'


class CommentsAdmin(admin.ModelAdmin):
    form = CommentsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'comment_body']
    # readonly_fields = ['name', 'slug', 'created', 'last_updated', 'comment_body']

admin.site.register(Comments, CommentsAdmin)


class NewsLetterAdminForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = '__all__'


class NewsLetterAdmin(admin.ModelAdmin):
    form = NewsLetterAdminForm


admin.site.register(NewsLetter, NewsLetterAdmin)
