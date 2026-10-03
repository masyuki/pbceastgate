from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_date",
        "start_time",
        "location",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "is_featured",
        "is_published",
        "event_date",
    )

    search_fields = (
        "title",
        "location",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "is_featured",
        "is_published",
    )

    date_hierarchy = "event_date"

    ordering = (
        "event_date",
        "start_time",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Event Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "event_date",
                    "start_time",
                    "end_time",
                    "location",
                )
            },
        ),

        (
            "Event Details",
            {
                "fields": (
                    "description",
                    "image",
                    "registration_url",
                )
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "is_featured",
                    "is_published",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
    )
