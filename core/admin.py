from django.contrib import admin

from .models import Certification, Education, Experience, Skill, SkillCategory


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "period", "is_current", "display_order")
    list_filter = ("is_current",)
    list_editable = ("display_order", "is_current")
    search_fields = ("role", "company", "summary", "highlights")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "earned", "is_in_progress", "display_order")
    list_filter = ("is_in_progress",)
    list_editable = ("display_order", "is_in_progress")
    search_fields = ("name", "issuer")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "period", "display_order")
    list_editable = ("display_order",)
    search_fields = ("degree", "school", "details")


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("name", "is_highlighted", "display_order")
    ordering = ("display_order", "name")


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "accent", "display_order", "show_on_home", "skill_count")
    list_filter = ("show_on_home", "accent")
    list_editable = ("display_order", "show_on_home")
    search_fields = ("name", "tagline", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SkillInline]

    @admin.display(description="Skills")
    def skill_count(self, obj):
        return obj.skills.count()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_highlighted", "display_order")
    list_filter = ("category", "is_highlighted")
    list_editable = ("is_highlighted", "display_order")
    search_fields = ("name",)
    autocomplete_fields = ("category",)
