from django.db import models
from django.utils import timezone


class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    responsible = models.CharField(max_length=250)
    manufacture = models.CharField(max_length=250, default='')
    department = models.CharField(max_length=250, default='')
    effect = models.FloatField()
    created = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
