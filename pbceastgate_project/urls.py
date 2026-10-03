"""
URL configuration for pbceastgate_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView

from apps.core.admin_dashboard import admin_dashboard
admin.site.site_header = "PBC Eastgate Administration"
admin.site.site_title = "PBC Eastgate Admin"
admin.site.index_title = "PBC Eastgate Administration"
urlpatterns = [
     path(
        "admin/dashboard/",
        admin_dashboard,
        name="admin-dashboard",
    ),

    path(
        "admin/",
        RedirectView.as_view(
            pattern_name="admin-dashboard",
            permanent=False,
        ),
    ),
    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        include("apps.core.urls"),
    ),
    path(
        "",
        include("apps.pages.urls"),
    ),
    path(
        "",
        include("apps.members.urls"),
    ),

    path(
        "",
        include("apps.sermons.urls"),
    ),
    path(
        "",
        include("apps.events.urls"),
    ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
