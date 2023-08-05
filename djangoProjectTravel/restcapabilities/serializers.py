from rest_framework import serializers

from djangoProjectTravel.destination.models import Destination


class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['destination_name', 'destination_photo', 'information', 'recommendation_to_visit']
        # fields = '__all__'
