from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Sermon


def sermon_list(request):
    sermons = (
        Sermon.objects
        .filter(is_published=True)
        .order_by("-sermon_date", "-created_at")
    )

    return render(
        request,
        "sermons/list.html",
        {
            "sermons": sermons,
        },
    )


def sermon_detail(request, slug):
    sermon = get_object_or_404(
        Sermon,
        slug=slug,
        is_published=True,
    )

    return render(
        request,
        "sermons/detail.html",
        {
            "sermon": sermon,
        },
    )
