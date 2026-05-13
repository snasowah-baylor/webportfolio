from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "email", "subject", "message"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-gray-900 placeholder-gray-400 shadow-sm transition focus:border-violet-500 focus:outline-none focus:ring-2 focus:ring-violet-200",
                    "placeholder": "Jane Doe",
                    "autocomplete": "name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-gray-900 placeholder-gray-400 shadow-sm transition focus:border-violet-500 focus:outline-none focus:ring-2 focus:ring-violet-200",
                    "placeholder": "jane@example.com",
                    "autocomplete": "email",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-gray-900 placeholder-gray-400 shadow-sm transition focus:border-violet-500 focus:outline-none focus:ring-2 focus:ring-violet-200",
                    "placeholder": "What's this about?",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-gray-900 placeholder-gray-400 shadow-sm transition focus:border-violet-500 focus:outline-none focus:ring-2 focus:ring-violet-200",
                    "placeholder": "Tell me about the role, project, or idea…",
                    "rows": 6,
                }
            ),
        }
        labels = {
            "full_name": "Full name",
            "email": "Email",
            "subject": "Subject",
            "message": "Message",
        }
