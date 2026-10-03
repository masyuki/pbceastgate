from django.contrib import admin

from .models import MemberProfile


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "membership_number",
        "membership_status",
        "date_joined",
        "allow_contact_requests",
    )

    list_filter = (
        "membership_status",
        "allow_contact_requests",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "membership_number",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
