from django import forms
from django.contrib.auth.models import User
from .models import Thread, Message


class MessageForm(forms.Form):
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Para",
        empty_label="-- Elegí un usuario --",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    body = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop("sender", None)
        super().__init__(*args, **kwargs)

    def save(self):
        if not self.sender:
            raise ValueError("Falta sender en el formulario")

        recipient = self.cleaned_data["recipient"]
        body = self.cleaned_data["body"]

        # Buscar si ya existe un hilo entre ambos
        thread = (
            Thread.objects.filter(participants=self.sender)
            .filter(participants=recipient)
            .distinct()
            .first()
        )

        # Si no existe, crearlo
        if not thread:
            thread = Thread.objects.create()
            thread.participants.add(self.sender, recipient)

        msg = Message.objects.create(
            thread=thread,
            sender=self.sender,
            body=body
        )

        return msg
