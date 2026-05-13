from django.shortcuts import get_object_or_404, render
from .models import Project


def projects_list(request):
    """List all projects."""
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/list.html", context)


def detail(request, slug):
    """Project case-study detail page."""
    project = get_object_or_404(Project, slug=slug)
    tools = [t.strip() for t in project.tools_used.split(",") if t.strip()]

    context = {
        "project": project,
        "tools": tools,
    }
    return render(request, "projects/detail.html", context)
