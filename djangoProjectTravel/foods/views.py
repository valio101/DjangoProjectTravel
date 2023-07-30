from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from djangoProjectTravel.destination.models import Destination
from djangoProjectTravel.foods.models import Food


class AddFood(CreateView):
    model = Food
    fields = ['food_name', 'food_photo', 'opinion', 'destination']
    success_url = reverse_lazy('index')
    template_name = 'foods/food-add-page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FoodDetailsView(DetailView):
    template_name = 'foods/food-details-page.html'
    model = Food

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.user
        return context


class EditFoodView(UpdateView):
    template_name = 'foods/food-edit-page.html'
    model = Food
    fields = ['food_name', 'food_photo', 'opinion', 'destination']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object.user
        return context

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details food', kwargs={
            'pk': self.object.pk,
        })


@login_required
def delete_food(request, pk):
    food = Food.objects.filter(pk=pk).get()
    if request.user == food.user:
        Destination.objects.filter(pk=food.pk).delete()
        food.save()
        food.delete()
        return redirect('index')
    return redirect('index')
