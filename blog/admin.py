from django.contrib import admin

from .models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "post_count")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

    @admin.display(description="Posts")
    def post_count(self, obj):
        return obj.posts.count()


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "is_published", "published_at")
    list_filter = ("is_featured", "is_published", "category")
    list_editable = ("is_featured", "is_published")
    search_fields = ("title", "excerpt", "body", "tags")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("category",)
    date_hierarchy = "published_at"
    readonly_fields = ("created_at", "updated_at")
