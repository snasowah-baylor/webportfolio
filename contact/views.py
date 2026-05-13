from django.shortcuts import render


def contact_form(request):
    """Display contact form."""
    context = {}
    return render(request, "contact/form.html", context)
