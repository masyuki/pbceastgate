from django.contrib import admin

from .models import Ministry


@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "leader",
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "leader",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "display_order",
        "name",
    )
