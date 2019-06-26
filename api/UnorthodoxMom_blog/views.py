from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView, View
from .models import Blog_Post, Products, Comments, NewsLetter
from .forms import Blog_PostForm, ProductsForm, CommentsForm, NewsLetterForm

catchall = TemplateView.as_view(template_name='base.html')

class Blog_PostListView(ListView):
    model = Blog_Post


class Blog_PostCreateView(CreateView):
    model = Blog_Post
    form_class = Blog_PostForm


class Blog_PostDetailView(DetailView):
    model = Blog_Post
    # lookup_field = 'slug'
    # extra_kwargs = {
    #     'url': {'lookup_field': 'slug'}
    # }

    def get_context_data(self, **kwargs):
        context = super(Blog_PostDetailView, self).get_context_data(**kwargs)
        context["blog_comments"] = Comments.objects.filter(blog_post=self.object.id)
        context["form"] = CommentsForm
        return context


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        blog_post_q = Blog_Post.objects.filter(slug=self.kwargs['slug'])
        comment_blog_post = blog_post_q.get().id
        if hasattr(self, 'object'):
            form_comment_data = {}
            for k,v in kwargs['data'].items():
                form_comment_data[k] = v

            form_comment_data['blog_post'] = comment_blog_post
            kwargs.update({'data': form_comment_data})
        return kwargs

    def get_success_url(self):
        return reverse_lazy('UnorthodoxMom_blog_blog_post_detail', kwargs={'slug': self.kwargs['slug']})


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


class PostCommentView(View):

    def get(self, request, *args, **kwargs):
         view = Blog_PostDetailView.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs) :
         view = CommentsCreateView.as_view()
         return view(request, *args, **kwargs) 