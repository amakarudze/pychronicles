from django import forms
from django.utils.translation import gettext_lazy as _

from django_recaptcha.fields import ReCaptchaField

from .validators import validate_email_message


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label=_("Full Name"),
        widget=(
            forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "FullName",
                    "placeholder": "Full Name",
                }
            )
        ),
    )
    email = forms.CharField(
        max_length=100,
        label=_("Email Address"),
        widget=(
            forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "EmailAddress",
                    "placeholder": "Email Address",
                }
            )
        ),
    )
    message = forms.CharField(
        max_length=100,
        label=_("Message"),
        widget=(
            forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "Message",
                    "rows": "5",
                    "placeholder": "Message",
                }
            )
        ),
    )
    captcha = ReCaptchaField()

    def clean_message(self):
        message = self.cleaned_data.get("message")
        validate_email_message(message)
        return message

    def send_email(self):
        subject = f"New contact message from {self.cleaned_data['name']}"
        message = self.cleaned_data['message']
        from_email = self.cleaned_data['email']
        recipient_list = [settings.DEFAULT_FROM_EMAIL]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
