from django.urls import include, path
from . import views

urlpatterns = [
    path('weeklydeals', views.WeeklyDealListCreateView.as_view(), name='weeklydeal-listcreate'),
    path('weeklydeals/<int:pk>', views.WeeklyDealDetailView.as_view(), name='weeklydeal-detail'),

    path('pastdeals', views.PastDealListCreateView.as_view(), name='pastdeal-listcreate'),
    path('pastdeals/<int:pk>', views.PastDealDetailView.as_view(), name='pastdeal-detail'),
]


