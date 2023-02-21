from django.contrib import admin
from Blog.models import Post
from Blog.models import Comment

# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display=['id','title','slug','author','body','publish','created','updated','status']
    list_filter=('status',)
    search_fields=('title','body',)
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active') 
    list_filter=('active','created','updated') 
    search_fields=('name','email','body')
admin.site.register(Post,AdminPost)
admin.site.register(Comment,CommentAdmin)
