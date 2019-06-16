import unittest
from django.urls import reverse
from django.test import Client
from .models import Blog_Post, Products, Comments, NewsLetter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_blog_post(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["post"] = "post"
    defaults["tags"] = "tags"
    defaults["images"] = "images"
    defaults["video_link"] = "video_link"
    defaults.update(**kwargs)
    if "product_list" not in defaults:
        defaults["product_list"] = create_products()
    if "blog_comments" not in defaults:
        defaults["blog_comments"] = create_comments()
    return Blog_Post.objects.create(**defaults)


def create_products(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["product_image"] = "product_image"
    defaults["product_link"] = "product_link"
    defaults.update(**kwargs)
    return Products.objects.create(**defaults)


def create_comments(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["comment_body"] = "comment_body"
    defaults.update(**kwargs)
    if "commenter" not in defaults:
        defaults["commenter"] = create_django_contrib_auth_models_user()
    return Comments.objects.create(**defaults)


def create_newsletter(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "newsletter_subscriber" not in defaults:
        defaults["newsletter_subscriber"] = create_django_contrib_auth_models_user()
    return NewsLetter.objects.create(**defaults)


class Blog_PostViewTest(unittest.TestCase):
    '''
    Tests for Blog_Post
    '''
    def setUp(self):
        self.client = Client()

    def test_list_blog_post(self):
        url = reverse('UnorthodoxMom_blog_blog_post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_blog_post(self):
        url = reverse('UnorthodoxMom_blog_blog_post_create')
        data = {
            "title": "title",
            "post": "post",
            "tags": "tags",
            "images": "images",
            "video_link": "video_link",
            "product_list": create_products().pk,
            "blog_comments": create_comments().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_blog_post(self):
        blog_post = create_blog_post()
        url = reverse('UnorthodoxMom_blog_blog_post_detail', args=[blog_post.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_blog_post(self):
        blog_post = create_blog_post()
        data = {
            "title": "title",
            "post": "post",
            "tags": "tags",
            "images": "images",
            "video_link": "video_link",
            "product_list": create_products().pk,
            "blog_comments": create_comments().pk,
        }
        url = reverse('UnorthodoxMom_blog_blog_post_update', args=[blog_post.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProductsViewTest(unittest.TestCase):
    '''
    Tests for Products
    '''
    def setUp(self):
        self.client = Client()

    def test_list_products(self):
        url = reverse('UnorthodoxMom_blog_products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_products(self):
        url = reverse('UnorthodoxMom_blog_products_create')
        data = {
            "name": "name",
            "product_image": "product_image",
            "product_link": "product_link",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_products(self):
        products = create_products()
        url = reverse('UnorthodoxMom_blog_products_detail', args=[products.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_products(self):
        products = create_products()
        data = {
            "name": "name",
            "product_image": "product_image",
            "product_link": "product_link",
        }
        url = reverse('UnorthodoxMom_blog_products_update', args=[products.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CommentsViewTest(unittest.TestCase):
    '''
    Tests for Comments
    '''
    def setUp(self):
        self.client = Client()

    def test_list_comments(self):
        url = reverse('UnorthodoxMom_blog_comments_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_comments(self):
        url = reverse('UnorthodoxMom_blog_comments_create')
        data = {
            "name": "name",
            "comment_body": "comment_body",
            "commenter": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_comments(self):
        comments = create_comments()
        url = reverse('UnorthodoxMom_blog_comments_detail', args=[comments.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_comments(self):
        comments = create_comments()
        data = {
            "name": "name",
            "comment_body": "comment_body",
            "commenter": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('UnorthodoxMom_blog_comments_update', args=[comments.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class NewsLetterViewTest(unittest.TestCase):
    '''
    Tests for NewsLetter
    '''
    def setUp(self):
        self.client = Client()

    def test_list_newsletter(self):
        url = reverse('UnorthodoxMom_blog_newsletter_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_newsletter(self):
        url = reverse('UnorthodoxMom_blog_newsletter_create')
        data = {
            "newsletter_subscriber": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_newsletter(self):
        newsletter = create_newsletter()
        url = reverse('UnorthodoxMom_blog_newsletter_detail', args=[newsletter.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_newsletter(self):
        newsletter = create_newsletter()
        data = {
            "newsletter_subscriber": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('UnorthodoxMom_blog_newsletter_update', args=[newsletter.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


