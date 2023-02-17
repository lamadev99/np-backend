from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.contrib.auth.models import User
from PIL import Image
from autoslug import AutoSlugField
from django.core.files.storage import default_storage
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Writer(models.Model):
    writer = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    bio = models.TextField()
    fUrl = models.CharField(max_length=255, null=True, blank=True)
    tUrl = models.CharField(max_length=255, null=True, blank=True)
    iUrl = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
            img.close()

    def __str__(self):
        return self.writer.username

class News(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', primary_key=True)
    category = models.CharField(max_length=255)
    subCategory = models.CharField(max_length=255)
    content = CKEditor5Field('Text', config_name='extends')
    keywords = models.CharField(max_length=255)
    metaWord = models.CharField(max_length=155)
    views = models.IntegerField(default=0)
    location = models.CharField(max_length=255, null=True, blank=True)

    is_video = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='news/', null=False, blank=False)
    alt = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 720 or img.width > 1280:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)
            img.close()

@receiver(post_delete, sender=News)
def delete_file(sender, instance, **kwargs):
    """Deletes file from filesystem when corresponding `MyModel` object is deleted."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    cId = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    comment = models.TextField()
    is_save = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NewsSubscription(models.Model):
    nsId = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)