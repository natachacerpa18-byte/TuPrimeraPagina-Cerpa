from django.urls import path
from .views import pages_dropdown, page_detail

urlpatterns = [
    path("", pages_dropdown, name="page_list"),
    path("<int:pk>/", page_detail, name="page_detail"),
]
