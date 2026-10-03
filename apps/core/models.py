from django.db import models


class SiteInformation(models.Model):
    church_name = models.CharField(
        max_length=200,
        default="PBC Eastgate"
    )

    tagline = models.CharField(
        max_length=255,
        blank=True
    )

    about_title = models.CharField(
        max_length=200,
        default="Who We Are"
    )

    about_content = models.TextField(
        blank=True
    )

    vision = models.TextField(
        blank=True
    )

    mission = models.TextField(
        blank=True
    )

    core_values = models.TextField(
        blank=True,
        help_text="Enter one core value per line."
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Site Information"
        verbose_name_plural = "Site Information"

    def __str__(self):
        return self.church_name


class Pastor(models.Model):

    name = models.CharField(
        max_length=200
    )

    title = models.CharField(
        max_length=200,
        help_text="Example: Lead Pastor"
    )

    bio = models.TextField(
        blank=True
    )

    photo = models.ImageField(
        upload_to="pastors/",
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
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
        return f"{self.name} — {self.title}"
    
class FinancialTransaction(models.Model):

    TRANSACTION_TYPE_CHOICES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    CATEGORY_CHOICES = [
        ("offering", "Offering"),
        ("tithe", "Tithe"),
        ("giving", "General Giving"),
        ("missions", "Missions"),
        ("building", "Building Fund"),
        ("project", "Project"),
        ("salary", "Salary"),
        ("utilities", "Utilities"),
        ("supplies", "Supplies"),
        ("other", "Other"),
    ]

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPE_CHOICES,
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="other",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    transaction_date = models.DateField()

    description = models.CharField(
        max_length=255,
        blank=True,
    )

    reference = models.CharField(
        max_length=100,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "-transaction_date",
            "-created_at",
        ]

    def __str__(self):
        return (
            f"{self.get_transaction_type_display()} - "
            f"KES {self.amount:,.2f}"
        )