from django.contrib import admin

from .models import ContentType, ContentTypeImage, NewsItem, Story


class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'page_name', 'title', 'tags', 'content')
    list_filter = ('page_name', 'active',)
    list_editable = ('page_name', 'title', 'tags', 'content')
    list_display_links = None
    search_fields = ('title',)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'genre', 'votes')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('votes',)


admin.site.register(ContentType, ContentTypeAdmin)
admin.site.register(ContentTypeImage)
admin.site.register(NewsItem)
