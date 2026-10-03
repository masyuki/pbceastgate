from django.contrib import admin

from .models import (
    SiteInformation,
    Pastor,
    FinancialTransaction,
)


@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):

    list_display = (
        "church_name",
        "tagline",
        "updated_at",
    )


@admin.register(Pastor)
class PastorAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "title",
    )

    ordering = (
        "display_order",
        "name",
    )


@admin.register(FinancialTransaction)
class FinancialTransactionAdmin(admin.ModelAdmin):

    list_display = (
        "transaction_date",
        "transaction_type",
        "category",
        "amount",
        "description",
    )

    list_filter = (
        "transaction_type",
        "category",
        "transaction_date",
    )

    search_fields = (
        "description",
        "reference",
        "notes",
    )

    ordering = (
        "-transaction_date",
        "-created_at",
    )

    date_hierarchy = "transaction_date"