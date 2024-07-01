from django.contrib import admin

from version.models import Version


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "version_number",
        "version_name",
        "version_is_active",
    )
    search_fields = (
        "product",
        "version_number",
        "version_name",
    )
