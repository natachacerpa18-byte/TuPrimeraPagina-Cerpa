from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup_view, profile_view, profile_edit, CustomPasswordChangeView

urlpatterns = [
    # auth
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", signup_view, name="signup"),

    # profile
    path("profile/", profile_view, name="profile"),
    path("profile/editar/", profile_edit, name="profile_edit"),
    path("profile/password/", CustomPasswordChangeView.as_view(), name="password_change"),
]
