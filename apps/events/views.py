from django.shortcuts import get_object_or_404, render

from .models import Event


def event_list(request):
    events = (
        Event.objects
        .filter(is_published=True)
        .order_by("event_date", "start_time")
    )

    return render(
        request,
        "events/list.html",
        {
            "events": events,
        },
    )


def event_detail(request, slug):
    event = get_object_or_404(
        Event,
        slug=slug,
        is_published=True,
    )

    return render(
        request,
        "events/detail.html",
        {
            "event": event,
        },
    )