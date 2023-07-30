from django.urls import path, include

from djangoProjectTravel.destination.views import AddDestination, DestinationDetailsView, EditDestinationView, \
    DestinationDeleteView

from django.contrib.auth.decorators import login_required

urlpatterns = (
    path('add/', login_required(AddDestination.as_view()), name='add destination'),
    path('<int:pk>/', include([
        path('', login_required(DestinationDetailsView.as_view()), name='details destination'),
        path('edit/', login_required(EditDestinationView.as_view()), name='edit destination'),
        path('delete/', login_required(DestinationDeleteView.as_view()), name='delete destination'),

    ])),
)
