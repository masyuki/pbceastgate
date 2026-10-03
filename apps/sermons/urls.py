from django.urls import path

from . import views


app_name = "sermons"


urlpatterns = [
    path(
        "sermons/",
        views.sermon_list,
        name="list",
    ),

    path(
        "sermons/<slug:slug>/",
        views.sermon_detail,
        name="detail",
    ),
]