from django.db import models

# Create your models here.

class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                .filter(status='published')


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    objects = models.Manager()

    def __str__(self):
        return  self.title