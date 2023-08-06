from django.urls import path

from djangoProjectTravel.common.views import IndexView, comment_photo, see_foods, see_photos, about_the_site

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('comment/<int:photo_id>', comment_photo, name='comment photo'),
    path('seephotos/', see_photos, name='see photos'),
    path('seefoods/', see_foods, name='see foods'),
    path('about/', about_the_site, name='about the site'),
)