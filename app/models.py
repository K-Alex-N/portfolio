from ckeditor.fields import RichTextField
from django.db import models

TYPE = (
    ('title', 'title'),
    ('progress_bar', 'progress_bar'),
    ('text', 'text'),
)


class Skill(models.Model):
    order = models.PositiveIntegerField()
    type = models.CharField(choices=TYPE)
    text = models.CharField(max_length=200)
    skill_score = models.PositiveIntegerField(null=True, blank=True)
    is_hidden = models.BooleanField(default=False)
    to_improve = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', ]


class Project(models.Model):
    short_title = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    description = RichTextField()
    link_to_site = models.CharField(max_length=500, blank=True)
    link_to_code = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['short_title']
