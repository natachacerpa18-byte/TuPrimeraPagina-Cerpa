from django.urls import path
from .views import (
    page_list,
    page_detail,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)

urlpatterns = [
    path("", page_list, name="page_list"),
    path("crear/", PageCreateView.as_view(), name="page_create"),
    path("<int:pk>/", page_detail, name="page_detail"),
    path("<int:pk>/editar/", PageUpdateView.as_view(), name="page_update"),
    path("<int:pk>/borrar/", PageDeleteView.as_view(), name="page_delete"),
]
