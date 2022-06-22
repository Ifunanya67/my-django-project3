from django.contrib import admin
from .models import Post

class PostDB(admin.ModelAdmin):
    list_display = [
        "title", "slug", "author", "body", "publish", "created", "updated", "status"
    ]


