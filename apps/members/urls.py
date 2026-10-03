from django.urls import path

from . import views


app_name = "members"


urlpatterns = [

    path(
        "members/login/",
        views.member_login,
        name="login",
    ),

    path(
        "members/signup/",
        views.member_signup,
        name="signup",
    ),

    path(
        "members/logout/",
        views.member_logout,
        name="logout",
    ),

    path(
        "members/",
        views.dashboard,
        name="dashboard",
    ),

]