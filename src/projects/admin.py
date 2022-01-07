from django.contrib import admin
from .models import ProjectPost, CategoryPost


class ProjectPostAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'content', 'slug', 'category')


admin.site.register(ProjectPost, ProjectPostAdmin)

class CategoryPostAdmin(admin.ModelAdmin):
    fields = ('title',)

admin.site.register(CategoryPost, CategoryPostAdmin)