from django.contrib import admin
from .models import ProjectPost


class ProjectPostAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'content', 'slug')


admin.site.register(ProjectPost, ProjectPostAdmin)