from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Blog_Post, Products, Comments, NewsLetter
from .forms import Blog_PostForm, ProductsForm, CommentsForm, NewsLetterForm

class Blog_PostListView(ListView):
    model = Blog_Post


class Blog_PostCreateView(CreateView):
    model = Blog_Post
    form_class = Blog_PostForm


class Blog_PostDetailView(DetailView):
    model = Blog_Post
    lookup_field = 'slug'


class Blog_PostUpdateView(UpdateView):
    model = Blog_Post
    form_class = Blog_PostForm


class ProductsListView(ListView):
    model = Products


class ProductsCreateView(CreateView):
    model = Products
    form_class = ProductsForm


class ProductsDetailView(DetailView):
    model = Products


class ProductsUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm


class CommentsListView(ListView):
    model = Comments


class CommentsCreateView(CreateView):
    model = Comments
    form_class = CommentsForm


class CommentsDetailView(DetailView):
    model = Comments


class CommentsUpdateView(UpdateView):
    model = Comments
    form_class = CommentsForm


class NewsLetterListView(ListView):
    model = NewsLetter


class NewsLetterCreateView(CreateView):
    model = NewsLetter
    form_class = NewsLetterForm


class NewsLetterDetailView(DetailView):
    model = NewsLetter


class NewsLetterUpdateView(UpdateView):
    model = NewsLetter
    form_class = NewsLetterForm

