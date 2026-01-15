from django.shortcuts import render, get_object_or_404
from web.models import Page  


def pages_dropdown(request):
    pages = Page.objects.all().order_by("titulo")
    return render(request, "pages/pages_dropdown.html", {"pages": pages})


def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, "pages/page_detail_simple.html", {"page": page})
