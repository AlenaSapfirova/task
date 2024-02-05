from django.contrib import admin
from .models import Post, User, Subscribtion



class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'header', 'body', 'date_created', 'author']
    list_display_links = None
    list_editable = ['header', 'body', 'author']

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'author']
    list_display_links = None
    list_editable = ['user', 'author']

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'id']
#     list_display_links = None
#     list_editable = ['email']    

admin.site.register(Post, PostAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(Subscribtion, SubscriptionAdmin)