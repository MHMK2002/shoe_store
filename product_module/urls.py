from django.urls import path
from .views import ProductView, WishListView

urlpatterns = [
    path('<int:pk>', ProductView.as_view()),
    path('', ProductView.as_view()),
    path('wish-list/<int:pk>', WishListView.as_view()),
]
