from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.MessageListCreateView.as_view()),
    path('message/<int:pk>', views.MessageDetailView.as_view())
    ]