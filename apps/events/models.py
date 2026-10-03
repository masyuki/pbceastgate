from django.db import models
from django.urls import reverse


class Event(models.Model):

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True
    )

    event_date = models.DateField()

    start_time = models.TimeField(
        blank=True,
        null=True
    )

    end_time = models.TimeField(
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    registration_url = models.URLField(
        blank=True,
        help_text="Optional link for event registration."
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "event_date",
            "start_time",
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "events:detail",
            kwargs={"slug": self.slug}
        )
