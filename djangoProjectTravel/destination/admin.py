from django.contrib import admin

from djangoProjectTravel.photos.models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    search_fields = ['destination_name']
    ordering = ['destination_name']
