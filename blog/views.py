from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import BlogCategory, BlogPost


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).select_related("category")

    query = (request.GET.get("q") or "").strip()
    if query:
        posts = posts.filter(
            Q(title__icontains=query)
            | Q(excerpt__icontains=query)
            | Q(body__icontains=query)
            | Q(tags__icontains=query)
        )

    category_slug = (request.GET.get("category") or "").strip()
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    featured = BlogPost.objects.filter(is_published=True, is_featured=True)[:3]
    categories = BlogCategory.objects.all()

    context = {
        "posts": posts,
        "featured_posts": featured,
        "categories": categories,
        "query": query,
        "active_category": category_slug,
    }
    return render(request, "blog/list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost.objects.select_related("category"),
        slug=slug,
        is_published=True,
    )
    post.tag_chips = post.tag_list()
    related = (
        BlogPost.objects.filter(is_published=True, category=post.category)
        .exclude(pk=post.pk)[:3]
        if post.category
        else BlogPost.objects.none()
    )
    return render(request, "blog/detail.html", {"post": post, "related_posts": related})
