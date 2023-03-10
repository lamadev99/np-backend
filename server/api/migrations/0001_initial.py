# Generated by Django 4.1.5 on 2023-02-20 05:33

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NewsSubscription',
            fields=[
                ('nsId', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('fUrl', models.CharField(blank=True, max_length=255, null=True)),
                ('tUrl', models.CharField(blank=True, max_length=255, null=True)),
                ('iUrl', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('writer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('title', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', primary_key=True, serialize=False)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('keywords', models.TextField(max_length=255)),
                ('metaWord', models.TextField(max_length=155)),
                ('views', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('is_video', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_writer_pick', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='news/')),
                ('alt', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.writer')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cId', models.AutoField(primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('comment', models.TextField()),
                ('is_save', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.news')),
            ],
        ),
    ]
