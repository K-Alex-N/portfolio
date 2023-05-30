from django.contrib import admin
from django.forms.widgets import Textarea

from .models import *


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {"widget": Textarea(attrs={'column': 150, 'rows': 3})},
    }


class SkillAdmin(admin.ModelAdmin):
    list_display_links = ['id']
    list_display = ['id', 'order', 'type', 'is_hidden', 'text', 'skill_score', 'to_improve']
    list_editable = ['order', 'type', 'text', 'skill_score', 'is_hidden', 'to_improve']

    class Media:
        css = {
            'all': ('admin/css/my_admin.css',)
        }


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
