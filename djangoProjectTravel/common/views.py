from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from djangoProjectTravel.common.forms import PhotoCommentForm, SearchPhotosForm
from djangoProjectTravel.common.models import PhotoComment
from djangoProjectTravel.destination.models import Destination
from djangoProjectTravel.foods.models import Food
from djangoProjectTravel.photos.models import Photo


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.all()
        context['comment_form'] = PhotoCommentForm
        return context


@login_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    if request.method == 'GET':
        form = PhotoCommentForm
    else:
        form = PhotoCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = photo
            comment.user = request.user
            comment.save()

    return redirect('details photo', pk=photo_id)


# class SeePhotosView(TemplateView):
#     template_name = 'common/see-photos.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['photos'] = Photo.objects.all()
#         context['comment_form'] = PhotoCommentForm
#         return context

def see_photos(request):
    photos = Photo.objects.all()

    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['search_by_destination_name']
    if search_pattern:
        photos = photos.filter(destination__destination_name__icontains=search_pattern)

    context = {
        'photos': photos,
        'search_form': SearchPhotosForm(),
        'comment_form': PhotoCommentForm(),
    }
    return render(request, 'common/see-photos.html', context)


def see_foods(request):
    foods = Food.objects.all()

    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['search_by_destination_name']
    if search_pattern:
        foods = foods.filter(destination__destination_name__icontains=search_pattern)

    context = {
        'foods': foods,
        'search_form': SearchPhotosForm(),
    }
    return render(request, 'common/see-foods.html', context)

