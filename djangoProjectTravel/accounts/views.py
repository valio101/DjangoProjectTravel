from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy

from djangoProjectTravel.accounts.forms import UserCreateForm
from django.contrib.auth.views import LoginView, LogoutView

from djangoProjectTravel.accounts.models import AppUser

UserModel = get_user_model()


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    photos_paginate_by = 2

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()
        photos = self.object.photo_set.order_by('-publication_date').all()
        # photos = Photo.objects.filter(user_id=self.object.id).order_by('publication_date')
        paginator = Paginator(photos, self.photos_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['destination_count'] = self.object.destination_set.count()
        context['photos_count'] = self.object.photo_set.count()
        # photos = self.object.photo_set.prefetch_related('photolike_set')
        # context['photos_count'] = photos.count()
        # context['likes_count'] = sum(x.photolike_set.count() for x in photos)
        context['photos'] = self.get_paginated_photos()
        context['destinations'] = self.object.destination_set.all
        # context['photos'] = self.object.photo_set.all()

        return context


class EditUserView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

