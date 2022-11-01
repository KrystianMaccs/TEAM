from django.contrib import admin

from .models import Posts, Comment


class PostsAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "author", "title", "body"]
    list_display_links = ["id", "pkid", "author"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "body", "post"]
    
admin.site.register(Posts, PostsAdmin)
admin.site.register(Comment, CommentAdmin)
