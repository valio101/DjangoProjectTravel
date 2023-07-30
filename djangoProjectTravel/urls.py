from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoProjectTravel.common.urls')),
    path('accounts/', include('djangoProjectTravel.accounts.urls')),
    path('destination/', include('djangoProjectTravel.destination.urls')),
    path('photos/', include('djangoProjectTravel.photos.urls')),
    path('foods/', include('djangoProjectTravel.foods.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)