from django.db import models
from django.core.urlresolvers import reverse
from embed_video.fields import EmbedVideoField

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    video = EmbedVideoField(default="")
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    objects = EntryQuerySet.as_manager()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

