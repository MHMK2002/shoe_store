from django.urls import path

from order_module import views

urlpatterns = [
    path('list/<str:completed>', views.OrderListView.as_view()),
    path('<int:pk>', views.OrderAPIView.as_view()),
    path('', views.OrderAPIView.as_view()),

]