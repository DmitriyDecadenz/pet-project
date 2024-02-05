from django.contrib import admin
from breaks.models.organisations import Organisations


@admin.register(Organisations)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "director")
