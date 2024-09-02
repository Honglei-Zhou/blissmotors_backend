from django.urls import include, path
from . import views

# router = DefaultRouter()
# router.register(r'car', views.CarViewSet)

urlpatterns = [
    path('cars/', include('cars.urls')),
    path('users/', include('users.urls')),
    path('leads/', include('leads.urls')),
    path('deals/', include('deals.urls')),
    path('careers/', include('careers.urls')),
    path('carts/', include('payment.urls')),
    path('chat/', include('chat.urls')),
]
