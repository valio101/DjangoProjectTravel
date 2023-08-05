from django.urls import path

from django.contrib.auth.decorators import login_required

from djangoProjectTravel.restcapabilities.views import DestinationsAsJSON

urlpatterns = (
    path('destinations/', login_required(DestinationsAsJSON.as_view()), name='api destinations'),
)
