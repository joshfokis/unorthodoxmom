from django.urls import path, include, re_path
from rest_framework import routers
from django.views.generic import TemplateView

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'blog_post', api.Blog_PostViewSet)
router.register(r'products', api.ProductsViewSet)
router.register(r'comments', api.CommentsViewSet)
router.register(r'newsletter', api.NewsLetterViewSet)


urlpatterns = [
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
    # path(r'^(?:.*)/?$', TemplateView.as_view(template_name='base.html')),
    # re_path(r'', views.catchall),
]

urlpatterns += [
    # urls for Blog_Post
    path('', views.Blog_PostListView.as_view(), name='UnorthodoxMom_blog_blog_post_list'),
    path('new/blog/', views.Blog_PostCreateView.as_view(), name='UnorthodoxMom_blog_blog_post_create'),
    path('blog/<slug:slug>/', views.PostCommentView.as_view(), name='UnorthodoxMom_blog_blog_post_detail'),
    path('blog/update/<slug:slug>/', views.Blog_PostUpdateView.as_view(), name='UnorthodoxMom_blog_blog_post_update'),
]

urlpatterns += [
    # urls for Products
    path('products/', views.ProductsListView.as_view(), name='UnorthodoxMom_blog_products_list'),
    path('products/create/', views.ProductsCreateView.as_view(), name='UnorthodoxMom_blog_products_create'),
    path('products/detail/<slug:slug>/', views.ProductsDetailView.as_view(), name='UnorthodoxMom_blog_products_detail'),
    path('products/update/<slug:slug>/', views.ProductsUpdateView.as_view(), name='UnorthodoxMom_blog_products_update'),
]

urlpatterns += [
    # urls for Comments
    path('comments/', views.CommentsListView.as_view(), name='UnorthodoxMom_blog_comments_list'),
    path('comments/create/', views.CommentsCreateView.as_view(), name='UnorthodoxMom_blog_comments_create'),
    path('comments/detail/<slug:slug>/', views.CommentsDetailView.as_view(), name='UnorthodoxMom_blog_comments_detail'),
    path('comments/update/<slug:slug>/', views.CommentsUpdateView.as_view(), name='UnorthodoxMom_blog_comments_update'),
]

urlpatterns += [
    # urls for NewsLetter
    path('newsletter/', views.NewsLetterListView.as_view(), name='UnorthodoxMom_blog_newsletter_list'),
    path('newsletter/create/', views.NewsLetterCreateView.as_view(), name='UnorthodoxMom_blog_newsletter_create'),
    path('newsletter/detail/<int:pk>/', views.NewsLetterDetailView.as_view(), name='UnorthodoxMom_blog_newsletter_detail'),
    path('newsletter/update/<int:pk>/', views.NewsLetterUpdateView.as_view(), name='UnorthodoxMom_blog_newsletter_update'),
]

