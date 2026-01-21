from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # Auth
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # Perfil
    path("profile/", views.profile_view, name="profile"),
    path("profile/editar/", views.profile_edit, name="profile_edit"),
    path("profile/password/", views.CustomPasswordChangeView.as_view(), name="password_change"),
]
