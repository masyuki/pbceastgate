from datetime import date
from decimal import Decimal

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from django.shortcuts import render

from apps.core.models import FinancialTransaction
from apps.members.models import MemberProfile


@staff_member_required
def admin_dashboard(request):

    today = date.today()

    total_members = MemberProfile.objects.count()

    visitors = MemberProfile.objects.filter(
        membership_status="visitor"
    ).count()

    members = MemberProfile.objects.filter(
        membership_status="member"
    ).count()

    active_members = MemberProfile.objects.filter(
        membership_status="active"
    ).count()

    inactive_members = MemberProfile.objects.filter(
        membership_status="inactive"
    ).count()

    new_this_month = MemberProfile.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month,
    ).count()

    income = (
        FinancialTransaction.objects
        .filter(transaction_type="income")
        .aggregate(total=Sum("amount"))
        ["total"]
        or Decimal("0.00")
    )

    expenses = (
        FinancialTransaction.objects
        .filter(transaction_type="expense")
        .aggregate(total=Sum("amount"))
        ["total"]
        or Decimal("0.00")
    )

    net_balance = income - expenses

    monthly_income = (
        FinancialTransaction.objects
        .filter(
            transaction_type="income",
            transaction_date__year=today.year,
            transaction_date__month=today.month,
        )
        .aggregate(total=Sum("amount"))
        ["total"]
        or Decimal("0.00")
    )

    monthly_expenses = (
        FinancialTransaction.objects
        .filter(
            transaction_type="expense",
            transaction_date__year=today.year,
            transaction_date__month=today.month,
        )
        .aggregate(total=Sum("amount"))
        ["total"]
        or Decimal("0.00")
    )

    yearly_income = (
        FinancialTransaction.objects
        .filter(
            transaction_type="income",
            transaction_date__year=today.year,
        )
        .aggregate(total=Sum("amount"))
        ["total"]
        or Decimal("0.00")
    )

    yearly_expenses = (
        FinancialTransaction.objects
        .filter(
            transaction_type="expense",
            transaction_date__year=today.year,
        )
        .aggregate(total=Sum("amount"))
        ["total"]
        or Decimal("0.00")
    )

    recent_transactions = (
        FinancialTransaction.objects
        .order_by("-transaction_date", "-created_at")[:10]
    )

    context = {
    "today": today,

    "total_members": total_members,
    "visitors": visitors,
    "members": members,
    "active_members": active_members,
    "inactive_members": inactive_members,
    "new_this_month": new_this_month,

    "income": income,
    "expenses": expenses,
    "net_balance": net_balance,

    "monthly_income": monthly_income,
    "monthly_expenses": monthly_expenses,

    "yearly_income": yearly_income,
    "yearly_expenses": yearly_expenses,

    "recent_transactions": recent_transactions,
}
    return render(
        request,
        "admin/dashboard.html",
        context,
    )