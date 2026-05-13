from django.db.models import Prefetch
from django.shortcuts import render

from blog.models import BlogPost
from projects.models import Project

from .models import Certification, Education, Experience, Skill, SkillCategory


def home(request):
    """Home page view with featured projects and Technical Expertise grid."""
    featured_projects = list(Project.objects.filter(is_featured=True)[:8])
    for project in featured_projects:
        project.tools_list = [
            t.strip() for t in (project.tools_used or "").split(",") if t.strip()
        ]

    expertise_categories = SkillCategory.objects.filter(show_on_home=True).prefetch_related(
        Prefetch(
            "skills",
            queryset=Skill.objects.filter(is_highlighted=True),
            to_attr="highlighted_skills",
        )
    )

    latest_posts = BlogPost.objects.filter(is_published=True).select_related("category")[:5]

    context = {
        "featured_projects": featured_projects,
        "expertise_categories": expertise_categories,
        "latest_posts": latest_posts,
    }
    return render(request, "core/index.html", context)


def about(request):
    """About page."""
    return render(request, "core/about.html", {})


def skills(request):
    """Skills page with categorized technical and leadership competencies."""
    skill_categories = SkillCategory.objects.prefetch_related("skills").all()
    context = {"skill_categories": skill_categories}
    return render(request, "core/skills.html", context)


def resume(request):
    """Resume page with experience, certifications, and education from DB."""
    experience = list(Experience.objects.all())
    for job in experience:
        job.highlights_list = job.highlight_list()

    context = {
        "experience": experience,
        "certifications": Certification.objects.filter(is_in_progress=False),
        "in_progress_certs": Certification.objects.filter(is_in_progress=True),
        "education": Education.objects.all(),
    }
    return render(request, "core/resume.html", context)
