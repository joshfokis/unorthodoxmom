# Generated by Django 2.2.2 on 2019-06-09 06:15

import UnorthodoxMom_blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('product_image', models.ImageField(upload_to=UnorthodoxMom_blog.models.get_image_path)),
                ('product_link', models.URLField(max_length=1000)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsletters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('comment_body', models.TextField(max_length=1000)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('post', models.TextField(max_length=10000)),
                ('tags', models.TextField(max_length=100)),
                ('images', models.ImageField(upload_to=UnorthodoxMom_blog.models.get_image_path)),
                ('video_link', models.TextField(max_length=1000)),
                ('blog_comments', models.ManyToManyField(related_name='blog_posts', to='UnorthodoxMom_blog.Comments')),
                ('product_list', models.ManyToManyField(related_name='blog_posts', to='UnorthodoxMom_blog.Products')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]