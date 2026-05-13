from django.shortcuts import render


def blog_list(request):
    """List all blog posts."""
    # Blog posts will be added later
    context = {}
    return render(request, "blog/list.html", context)
