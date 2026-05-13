from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out — your message is in. I'll reply to your email shortly.",
            )
            return redirect("contact:form")
    else:
        form = ContactForm()

    return render(request, "contact/form.html", {"form": form})
