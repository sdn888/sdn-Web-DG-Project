from django.contrib import admin
from .models import News_post

class News_postAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')

admin.site.register(News_post, News_postAdmin)



