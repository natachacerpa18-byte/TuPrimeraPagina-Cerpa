from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from web.models import Page


def page_list(request):
    pages = Page.objects.all().order_by("titulo")
    return render(request, "pages/page_list.html", {"pages": pages})


def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, "pages/page_detail_simple.html", {"page": page})


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("page_list")


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "pages/page_form.html"

    def get_success_url(self):
        return reverse_lazy("page_detail", kwargs={"pk": self.object.pk})


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("page_list")
