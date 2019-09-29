from django.contrib import admin
from .models import Forum, Thread, Post


class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'forum_type', 'forum')
    list_filter = ('forum_type', 'issubforum')

admin.site.register(Forum, ForumAdmin)                              #shows the forums that are created in the database
admin.site.register(Thread)                                         #shows the threads that are created in the database
admin.site.register(Post)                                           #shows the posts that are created in the database

#TODO: filter parent forums and subforums to seperate table views
#TODO: make better admin interface