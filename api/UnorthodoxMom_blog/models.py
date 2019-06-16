from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ImageField
from django.db.models import TextField
from django.db.models import URLField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields

import os

def get_image_path(request, filename):
    print(request)
    print(filename)
    return os.path.join('uploads', filename.replace(" ", "_"))

class Blog_Post(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    post = models.TextField(max_length=10000)
    tags = models.TextField(max_length=100)
    images = models.ImageField(upload_to=get_image_path, blank=True)
    video_link = models.TextField(max_length=1000, blank=True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('UnorthodoxMom_blog_blog_post_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('UnorthodoxMom_blog_blog_post_update', args=(self.slug,))


class Products(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    product_image = models.ImageField(upload_to=get_image_path)
    product_link = models.URLField(max_length=1000)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('UnorthodoxMom_blog_products_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('UnorthodoxMom_blog_products_update', args=(self.slug,))


class Comments(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    comment_body = models.TextField(max_length=1000)

    # Relationship Fields
    blog_post = models.ForeignKey(
        'UnorthodoxMom_blog.Blog_Post',
        on_delete=models.CASCADE, related_name="commentss", default=0 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('UnorthodoxMom_blog_comments_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('UnorthodoxMom_blog_comments_update', args=(self.slug,))


class NewsLetter(models.Model):


    # Relationship Fields
    newsletter_subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="newsletters", 
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('UnorthodoxMom_blog_newsletter_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('UnorthodoxMom_blog_newsletter_update', args=(self.pk,))

