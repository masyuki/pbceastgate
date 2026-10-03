from django.conf import settings
from django.db import models


class MemberProfile(models.Model):

    MEMBERSHIP_STATUS_CHOICES = [
        ("visitor", "Visitor"),
        ("member", "Member"),
        ("active", "Active Member"),
        ("inactive", "Inactive Member"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="member_profile",
    )

    membership_number = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    membership_status = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_STATUS_CHOICES,
        default="visitor",
    )

    date_joined = models.DateField(
        blank=True,
        null=True,
    )

    profile_photo = models.ImageField(
        upload_to="members/profiles/",
        blank=True,
        null=True,
    )

    allow_contact_requests = models.BooleanField(
        default=True,
        help_text="Allow other members to request contact through the church.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username
