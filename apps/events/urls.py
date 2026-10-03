from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("events/", views.event_list, name="list"),
    path("events/<slug:slug>/", views.event_detail, name="detail"),
]
