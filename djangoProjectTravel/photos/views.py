from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from djangoProjectTravel.common.forms import PhotoCommentForm
from djangoProjectTravel.common.models import PhotoComment
from djangoProjectTravel.destination.models import Destination
from djangoProjectTravel.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from djangoProjectTravel.photos.models import Photo

import time


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('details photo', pk=photo.pk)

    context = {'form': form, }

    return render(request, 'photos/photo-add-page.html', context)


@login_required
def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        comment_form = PhotoCommentForm
    else:
        comment_form = PhotoCommentForm(request.POST)

        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.photo = photo
            comment_form.user = request.user
            comment_form.save()

    context = {
        'photo': photo,
        'is_owner': request.user == photo.user,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


@login_required()
def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        # request.method == 'POST':
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)
    context = {
        'form': form,
        'photo': photo,
        'is_owner': request.user == photo.user,
    }

    return render(request, 'photos/photo-edit-page.html', context)


#
#
# def delete_photo(request, pk):
#     photo = Photo.objects.filter(pk=pk).get()
#
#     photo.tagged_pets.clear() # many to many
#     PhotoLike.objects.filter(photo_id=photo.id).delete() # one to many
#     PhotoComment.objects.filter(photo_id=photo.id).delete() # one to many
#     photo.save()
#     photo.delete()
#     return redirect('index')


@login_required()
def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.user == photo.user:
        # Destination.objects.filter(pk=photo.pk).delete()
        PhotoComment.objects.filter(photo_id=photo.id).delete()
        photo.save()
        photo.delete()
        return redirect('index')
    return redirect('index')
