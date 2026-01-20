from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView

from .models import Thread, Message
from .forms import MessageForm


class InboxView(LoginRequiredMixin, ListView):
    model = Thread
    template_name = "mensajeria/inbox.html"
    context_object_name = "threads"

    def get_queryset(self):
        return Thread.objects.filter(participants=self.request.user).order_by("-updated_at")


class ThreadDetailView(LoginRequiredMixin, View):
    template_name = "mensajeria/thread_detail.html"

    def get(self, request, pk):
        thread = get_object_or_404(Thread, pk=pk, participants=request.user)
        messages = thread.messages.order_by("created_at")

        form = forms = MessageForm(sender=request.user)

        return render(request, self.template_name, {
            "thread": thread,
            "messages": messages,
            "form": form
        })

    def post(self, request, pk):
        thread = get_object_or_404(Thread, pk=pk, participants=request.user)
        form = MessageForm(request.POST, sender=request.user)

        if form.is_valid():
            # En este caso ignoramos recipient porque ya estamos dentro del thread
            Message.objects.create(
                thread=thread,
                sender=request.user,
                body=form.cleaned_data["body"]
            )
            return redirect("thread_detail", pk=thread.pk)

        messages = thread.messages.order_by("created_at")
        return render(request, self.template_name, {
            "thread": thread,
            "messages": messages,
            "form": form
        })


class MessageCreateView(LoginRequiredMixin, View):
    template_name = "mensajeria/message_form.html"

    def get(self, request):
        form = MessageForm(sender=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = MessageForm(request.POST, sender=request.user)

        if form.is_valid():
            msg = form.save()
            return redirect("thread_detail", pk=msg.thread.pk)

        return render(request, self.template_name, {"form": form})
