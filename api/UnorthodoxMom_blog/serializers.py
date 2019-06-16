from . import models

from rest_framework import serializers


class Blog_PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog_Post
        fields = (
            '__all__'
        )
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }



class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Products
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'product_image', 
            'product_link', 
        )


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comments
        fields = (
            '__all__'
        )
        lookup_field = 'blog_post'
        extra_kwargs = {
            'url': {'lookup_field': 'blog_post'}
        }



class NewsLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NewsLetter
        fields = (
            '__all__'
        )
