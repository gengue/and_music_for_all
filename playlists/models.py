from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    """
    Una clase abstracta que registra la fecha de creacion y
    modificacion del modelo
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    modified = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    class Meta:
        abstract = True


MEDIA_CHOICES = (
    ('YOUTUBE', 'YOUTUBE'),
    ('SOUNCLOUD', 'SOUNDCLOUD'),
    ('VIMEO', 'VIMEO'),
)

class Category(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u'%s' % self.name


class Playlist(TimeStampedModel):
    title       = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category    = models.ForeignKey(Category)
    user        = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.title


class Song(TimeStampedModel):
    url         = models.CharField(max_length=500)
    media_type  = models.CharField(max_length=255, choices=MEDIA_CHOICES)
    playlist    = models.ForeignKey(Playlist)

    def __unicode__(self):
        return u'%s' % self.url


