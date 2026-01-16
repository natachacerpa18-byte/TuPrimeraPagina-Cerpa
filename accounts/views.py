from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # crea profile si no existe
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect("profile")
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False, label="Nombre", widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=False, label="Apellido", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=False, label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = Profile
        fields = ("avatar", "bio", "birth_date")
        labels = {
            "avatar": "Avatar",
            "bio": "Biografía",
            "birth_date": "Fecha de nacimiento",
        }
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        self.user = user
        self.fields["avatar"].required = False

        if user:
            self.fields["first_name"].initial = user.first_name
            self.fields["last_name"].initial = user.last_name
            self.fields["email"].initial = user.email

        # bootstrap para el file input
        self.fields["avatar"].widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        profile = super().save(commit=False)
        if self.user:
            self.user.first_name = self.cleaned_data.get("first_name", "")
            self.user.last_name = self.cleaned_data.get("last_name", "")
            self.user.email = self.cleaned_data.get("email", "")
            if commit:
                self.user.save()

        if commit:
            profile.save()
        return profile


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})


@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile, user=request.user)

    return render(request, "accounts/profile_edit.html", {"form": form})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("profile")
