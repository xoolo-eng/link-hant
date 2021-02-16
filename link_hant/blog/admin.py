from django.contrib import admin
from blog.models import Blog, Tags, Comment


class AdminBlog(admin.ModelAdmin):
    class Meta:
        list_display = ["title", "user"]


class AdminTags(admin.ModelAdmin):
    class Meta:
        list_display = ["name", "id"]


admin.site.register(Blog, AdminBlog)
admin.site.register(Tags, AdminTags)
admin.site.register(Comment)