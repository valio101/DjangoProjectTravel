from django.urls import path, include

from djangoProjectTravel.accounts.views import SignUpView, SignInView, SignOutView, UserDetailsView, EditUserView, \
    UserDeleteView

from .signals import *

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/'
         '', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)


