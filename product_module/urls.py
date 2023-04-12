from django.urls import path
from .views import ProductView, WishListView, ProductViewURD

urlpatterns = [
    path('<int:pk>', ProductView.as_view()),
    path('', ProductView.as_view()),
    path('', ProductViewURD.as_view()),
    path('<int:pk>', ProductViewURD.as_view()),
    path('wish-list/<int:pk>', WishListView.as_view()),
    path('filter', ProductView.as_view()),
]
