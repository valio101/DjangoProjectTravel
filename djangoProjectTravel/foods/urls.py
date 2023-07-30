from django.urls import path, include

from djangoProjectTravel.foods.views import AddFood, FoodDetailsView, EditFoodView, delete_food

from django.contrib.auth.decorators import login_required

urlpatterns = (
    path('add/', login_required(AddFood.as_view()), name='add food'),
    path('<int:pk>/', include([
        path('', login_required(FoodDetailsView.as_view()), name='details food'),
        path('edit/', login_required(EditFoodView.as_view()), name='edit food'),
        path('delete/', delete_food, name='delete food'),
    ]))
)
