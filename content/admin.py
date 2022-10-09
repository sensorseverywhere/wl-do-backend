from django.contrib import admin

from .models import Content, ContentImage, NewsItem, Story


class ContentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'name', 'title', 'type', 'content')
    list_filter = ('name', 'active',)
    list_editable = ('name', 'title', 'type', 'content')
    list_display_links = None
    search_fields = ('title',)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'genre', 'votes')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('votes',)


admin.site.register(Content, ContentAdmin)
admin.site.register(ContentImage)
admin.site.register(NewsItem)
