# Register your models here.
from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'pub_date', 'username')
    list_filter = ('pub_date', 'username')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'