from django.urls import path
from .views import InboxView, ThreadDetailView, MessageCreateView

urlpatterns = [
    path("", InboxView.as_view(), name="inbox"),
    path("nuevo/", MessageCreateView.as_view(), name="message_create"),
    path("<int:pk>/", ThreadDetailView.as_view(), name="thread_detail"),
]
