from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "display_order", "created_at")
    list_filter = ("category", "is_featured", "created_at")
    search_fields = ("title", "summary", "description")
    ordering = ("-is_featured", "display_order", "-created_at")
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "summary",
                    "category",
                    "is_featured",
                    "display_order",
                )
            },
        ),
        (
            "Content",
            {
                "fields": (
                    "description",
                    "key_features",
                    "role_contribution",
                    "challenges",
                    "lessons_learned",
                )
            },
        ),
        ("Technical Details", {"fields": ("tools_used",)}),
        ("Media & Links", {"fields": ("image", "github_link", "demo_link")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
    readonly_fields = ("created_at", "updated_at")
