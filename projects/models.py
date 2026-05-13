from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """
    Model for storing portfolio projects.
    """

    CATEGORY_CHOICES = [
        ("AI", "AI & Machine Learning"),
        ("WEB", "Web Development"),
        ("DATA", "Data Science"),
        ("CYBERSECURITY", "Cybersecurity"),
        ("CLOUD", "Cloud & DevOps"),
        ("AUTO", "Automation"),
        ("DevOps", "DevOps/DevSecOps"),
        ("Digital", "Digital Transformation"),
        ("PM", "Project Management"),
        ("Cyber", "Cybersecurity/Risk Management"),
        ("OTHER", "Other"),
    ]

    title = models.CharField(max_length=200, help_text="Project title")
    slug = models.SlugField(
        unique=True, blank=True, help_text="URL slug (auto-generated from title)"
    )
    summary = models.CharField(max_length=500, help_text="One-sentence project summary")
    description = models.TextField(
        help_text="Detailed project description including business problem"
    )
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, help_text="Project category"
    )
    tools_used = models.CharField(
        max_length=500, help_text="Comma-separated list of tools and technologies"
    )
    key_features = models.TextField(help_text="Key features and accomplishments")
    role_contribution = models.TextField(
        help_text="Your role and contribution to the project"
    )
    challenges = models.TextField(
        help_text="Biggest challenges faced during the project"
    )
    lessons_learned = models.TextField(help_text="What you learned from the project")
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        help_text="Project screenshot or visual",
    )
    github_link = models.URLField(
        blank=True, null=True, help_text="Link to GitHub repository"
    )
    demo_link = models.URLField(
        blank=True, null=True, help_text="Link to live demo or deployed project"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="When the project was added"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="When the project was last updated"
    )
    is_featured = models.BooleanField(
        default=False, help_text="Display on home page as featured project"
    )
    display_order = models.IntegerField(
        default=0, help_text="Order in which to display projects"
    )

    class Meta:
        ordering = ["-is_featured", "display_order", "-created_at"]
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "project"
            slug = base
            n = 2
            qs = Project.objects.exclude(pk=self.pk)
            while qs.filter(slug=slug).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)
