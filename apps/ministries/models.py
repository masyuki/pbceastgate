from django.db import models


class Ministry(models.Model):

    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True
    )

    short_description = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    leader = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to="ministries/",
        blank=True,
        null=True
    )

    contact_email = models.EmailField(
        blank=True
    )

    meeting_information = models.TextField(
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name
