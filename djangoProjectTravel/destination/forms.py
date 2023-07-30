from django import forms

from djangoProjectTravel.destination.models import Destination


class DestinationBaseForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'


class DestinationCreateForm(DestinationBaseForm):
    pass


class DestinationEditForm(DestinationBaseForm):
    pass
