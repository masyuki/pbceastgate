from django.shortcuts import render
from apps.events.models import Event
from apps.sermons.models import Sermon
from .models import SiteInformation, Pastor

def home(request):
    latest_sermon = (
        Sermon.objects
        .filter(is_published=True)
        .order_by("-sermon_date")
        .first()
    )

    upcoming_events = (
        Event.objects
        .filter(is_published=True)
        .order_by("event_date", "start_time")[:3]
    )

    return render(
        request,
        "core/home.html",
        {
            "latest_sermon": latest_sermon,
            "upcoming_events": upcoming_events,
        },
    )

def about(request):
    site_info = SiteInformation.objects.first()

    pastors = Pastor.objects.filter(
        is_active=True
    ).order_by(
        "display_order",
        "name"
    )

    return render(
        request,
        "core/about.html",
        {
            "site_info": site_info,
            "pastors": pastors,
        }
    )