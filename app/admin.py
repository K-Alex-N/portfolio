from django.contrib import admin

from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display_links = ['id']
    list_display = ['id', 'order', 'type', 'is_hidden', 'text', 'skill_score', 'to_improve']
    list_editable = ['order', 'type', 'text', 'skill_score', 'is_hidden', 'to_improve']

    class Media:
        css = {
            'all': ('admin/css/my_admin.css',)
        }


admin.site.register(Project)
admin.site.register(Skill, SkillAdmin)
