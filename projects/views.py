from django.shortcuts import get_object_or_404, render

from .models import Project


def _split_tools(value: str) -> list[str]:
    return [t.strip() for t in (value or "").split(",") if t.strip()]


def projects_list(request):
    """List all projects."""
    projects = list(Project.objects.all())
    for project in projects:
        project.tools_list = _split_tools(project.tools_used)
    return render(request, "projects/list.html", {"projects": projects})


def detail(request, slug):
    """Project case-study detail page."""
    project = get_object_or_404(Project, slug=slug)
    project.tools_list = _split_tools(project.tools_used)
    return render(request, "projects/detail.html", {"project": project})
