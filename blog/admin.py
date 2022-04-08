from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','date_create','date_edit')
    ordering = ('title','date_create',)
    # list_display_links = ['author']
    # list_editable = ('title',)

# admin.site.register(Post , Post)
