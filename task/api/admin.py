from django.contrib import admin
from .models import Post, Subscribtion


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'header', 'body', 'date_created', 'author']
    list_display_links = None
    list_editable = ['header', 'body', 'author']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'author']
    list_display_links = None
    list_editable = ['user', 'author']

 
admin.site.register(Post, PostAdmin)
admin.site.register(Subscribtion, SubscriptionAdmin)
