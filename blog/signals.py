from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post

@receiver(pre_save, render=Post)
def pre_save_create_slug(render, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + " " + instance.title)
