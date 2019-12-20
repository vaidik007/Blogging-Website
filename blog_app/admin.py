from django.contrib import admin
from .models import blog_post
# Register your models here.

class post_field(admin.ModelAdmin):
    list_display = ('Post_Title', 'Slug','created_on')
    search_fields = ('Post_Title' ,'Slug')
    prepopulated_fields = {'Slug': ('Post_Title',) }

admin.site.register(blog_post,post_field)
