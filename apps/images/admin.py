from django.contrib import admin
from django.utils.html import format_html
from .models import Image, Tag, ImageTag, Search


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('query', 'status', 'created_at')
    search_fields = ('query',)
    list_filter = ('status',)


class ImageTagInline(admin.TabularInline):
    model = ImageTag
    extra = 0
    readonly_fields = ('image', 'tag')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', "admin_thumbnail")
    search_fields = ('title',)
    inlines = [ImageTagInline]
    readonly_fields = ('admin_thumbnail',)
    list_per_page = 250

    def admin_thumbnail(self, obj):
        return format_html(f'<img src="{obj.url}" style="max-width: 200px; max-height: 200px;" />')

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 250


@admin.register(ImageTag)
class ImageTagAdmin(admin.ModelAdmin):
    list_display = ('image', 'tag')
    search_fields = ('image__title', 'tag__name')
    autocomplete_fields = ('image', 'tag')
    list_per_page = 250
