from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'published']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'content']