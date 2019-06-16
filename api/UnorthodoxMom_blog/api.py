from . import models
from . import serializers
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class Blog_PostViewSet(viewsets.ModelViewSet):
    """ViewSet for the Blog_Post class"""

    queryset = models.Blog_Post.objects.all()
    serializer_class = serializers.Blog_PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductsViewSet(viewsets.ModelViewSet):
    """ViewSet for the Products class"""

    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentsViewSet(viewsets.ModelViewSet):
    """ViewSet for the Comments class"""
    
    queryset = models.Comments.objects.all()
    # queryset = get_queryset(self)
    serializer_class = serializers.CommentsSerializer
    lookup_field = 'blog_post'
    extra_kwargs = {
        'url': {'lookup_field': 'blog_post'}
    }
    
    # permission_classes = [permissions.IsAuthenticated]
    


class NewsLetterViewSet(viewsets.ModelViewSet):
    """ViewSet for the NewsLetter class"""

    queryset = models.NewsLetter.objects.all()
    serializer_class = serializers.NewsLetterSerializer
    permission_classes = [permissions.IsAuthenticated]


