from django.contrib import admin

from djangoProjectTravel.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'destination')
    list_filter = ("destination",)


