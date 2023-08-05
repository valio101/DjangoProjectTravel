from rest_framework.generics import ListAPIView

from djangoProjectTravel.destination.models import Destination
from djangoProjectTravel.restcapabilities.serializers import DestinationsSerializer


# Create your views here.

class DestinationsAsJSON(ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationsSerializer

# http://127.0.0.1:8000/api/destinations/

