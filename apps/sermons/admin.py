from django.contrib import admin

from .models import Sermon

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "speaker",
        "sermon_date",
        "youtube_status",
        "is_published",
        "is_featured",
    )

    list_filter = (
        "is_published",
        "is_featured",
        "category",
        "sermon_date",
    )

    search_fields = (
        "title",
        "speaker",
        "description",
        "scripture",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    ordering = (
        "-sermon_date",
    )

    fieldsets = (
        (
            "Sermon Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "speaker",
                    "sermon_date",
                    "category",
                    "scripture",
                    "description",
                )
            },
        ),

        (
            "Video & Audio",
            {
                "fields": (
                    "youtube_url",
                    "audio_url",
                    "video_url",
                    "thumbnail",
                )
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                )
            },
        ),
    )

    @admin.display(
        boolean=True,
        description="YouTube"
    )
    def youtube_status(self, obj):
        return bool(obj.youtube_url)