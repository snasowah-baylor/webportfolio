from django.db import models
from django.utils.text import slugify


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    period = models.CharField(
        max_length=80,
        help_text='Human-readable period, e.g. "2023 — Present".',
    )
    summary = models.TextField(
        blank=True,
        help_text="Short paragraph shown on the About timeline.",
    )
    highlights = models.TextField(
        blank=True,
        help_text="One highlight per line. Shown as bullet list on resume page.",
    )
    is_current = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-is_current"]

    def __str__(self):
        return f"{self.role} — {self.company}"

    def highlight_list(self):
        return [line.strip() for line in self.highlights.splitlines() if line.strip()]


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    earned = models.CharField(
        max_length=80,
        blank=True,
        help_text='Date or status, e.g. "April 2026" or "In progress".',
    )
    is_in_progress = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["is_in_progress", "display_order", "name"]

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    period = models.CharField(
        max_length=80,
        blank=True,
        help_text='e.g. "Expected December 2026".',
    )
    details = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.degree} — {self.school}"


class SkillCategory(models.Model):
    ACCENT_CHOICES = [
        ("violet", "Violet"),
        ("indigo", "Indigo"),
        ("blue", "Blue"),
        ("sky", "Sky"),
        ("purple", "Purple"),
        ("fuchsia", "Fuchsia"),
        ("rose", "Rose"),
        ("emerald", "Emerald"),
        ("green", "Green"),
        ("amber", "Amber"),
        ("red", "Red"),
        ("gray", "Gray"),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    tagline = models.CharField(
        max_length=300,
        help_text="One-line summary shown on the Skills page.",
    )
    description = models.TextField(
        blank=True,
        help_text="Short paragraph shown on the home page expertise card. Falls back to tagline if blank.",
    )
    accent = models.CharField(
        max_length=20,
        choices=ACCENT_CHOICES,
        default="violet",
        help_text="Tailwind color token used for the card's icon, chips, and accents.",
    )
    icon_svg_path = models.TextField(
        blank=True,
        help_text='SVG path "d" attribute for the category icon (no <svg> wrapper).',
    )
    display_order = models.IntegerField(default=0)
    show_on_home = models.BooleanField(
        default=True,
        help_text="Display this category card in the home page Technical Expertise grid.",
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name_plural = "Skill categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name) or "category"
            slug = base
            n = 2
            qs = SkillCategory.objects.exclude(pk=self.pk)
            while qs.filter(slug=slug).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory, on_delete=models.CASCADE, related_name="skills"
    )
    name = models.CharField(max_length=80)
    is_highlighted = models.BooleanField(
        default=False,
        help_text="Show this skill as a chip on the home page category card (top picks).",
    )
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]
        unique_together = [("category", "name")]

    def __str__(self):
        return f"{self.name} ({self.category.name})"
