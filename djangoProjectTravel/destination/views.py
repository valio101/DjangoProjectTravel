from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views import generic as views

from djangoProjectTravel.common.models import PhotoComment
from djangoProjectTravel.destination.forms import DestinationEditForm
from djangoProjectTravel.destination.models import Destination
from djangoProjectTravel.photos.models import Photo


class AddDestination(CreateView):
    model = Destination
    fields = ['destination_name', 'destination_photo', 'information', 'recommendation_to_visit']
    success_url = reverse_lazy('index')
    template_name = 'destination/destination-add-page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DestinationDetailsView(views.DetailView):
    template_name = 'destination/destination-details-page.html'
    model = Destination
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.user
        return context


class EditDestinationView(UpdateView):
    template_name = 'destination/destination-edit-page.html'
    model = Destination
    fields = ('destination_name', 'destination_photo', 'information', 'recommendation_to_visit',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.user
        return context

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details destination', kwargs={
            'pk': self.object.pk,
        })


class DestinationDeleteView(views.DeleteView):
    template_name = 'destination/destination-delete-page.html'
    model = Destination
    fields = ('destination_name', 'destination_photo', 'information', 'recommendation_to_visit',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.user
        return context

    success_url = reverse_lazy('index')
