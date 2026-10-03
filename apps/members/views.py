from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render

from .models import MemberProfile


def member_login(request):

    if request.user.is_authenticated:
        return redirect("members:dashboard")

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            return redirect(
                "members:dashboard"
            )

        return render(
            request,
            "members/login.html",
            {
                "error": "Invalid username or password.",
                "username": username,
            },
        )

    return render(
        request,
        "members/login.html",
    )


def member_signup(request):

    if request.user.is_authenticated:
        return redirect("members:dashboard")

    if request.method == "POST":

        first_name = request.POST.get(
            "first_name",
            ""
        ).strip()

        last_name = request.POST.get(
            "last_name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip().lower()

        password = request.POST.get(
            "password",
            ""
        )

        password_confirm = request.POST.get(
            "password_confirm",
            ""
        )

        errors = []

        if not first_name:
            errors.append("Please enter your first name.")

        if not last_name:
            errors.append("Please enter your last name.")

        if not email:
            errors.append("Please enter your email address.")

        if not password:
            errors.append("Please enter a password.")

        if password != password_confirm:
            errors.append("The passwords do not match.")

        if User.objects.filter(
            email__iexact=email
        ).exists():
            errors.append(
                "An account with this email address already exists."
            )

        if errors:

            return render(
                request,
                "members/signup.html",
                {
                    "errors": errors,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                },
            )

        # Use email as the username.
        username = email

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                "members/signup.html",
                {
                    "errors": [
                        "An account with this email address already exists."
                    ],
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                },
            )

        with transaction.atomic():

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            MemberProfile.objects.create(
                user=user,
                membership_status="visitor",
            )

        login(
            request,
            user,
        )

        return redirect(
            "members:dashboard"
        )

    return render(
        request,
        "members/signup.html",
    )


@login_required
def dashboard(request):

    return render(
        request,
        "members/dashboard.html",
    )


@login_required
def member_logout(request):

    logout(request)

    return redirect(
        "members:login"
    )