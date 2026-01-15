from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Page


class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"
    context_object_name = "pages"


class PageDetailView(DetailView):
    model = Page
    template_name = "pages/pages_detail.html"
    context_object_name = "page"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "pages/pages_form.html"
    success_url = reverse_lazy("page_list")

    def form_valid(self, form):
        if hasattr(form.instance, "autor_id"):
            form.instance.autor = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = "pages/pages_form.html"

    def get_success_url(self):
        return reverse_lazy("page_detail", kwargs={"pk": self.object.pk})


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "pages/pages_confirm_delete.html"
    success_url = reverse_lazy("page_list")
