from django.urls import include, path
from . import views

urlpatterns = [
    path('products', views.ProductListCreateView.as_view(), name='product-listcreate'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('orders', views.OrderListCreateView.as_view(), name='order-listcreate'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('payments', views.PaymentListCreateView.as_view(), name='payment-listcreate'),
    path('payments/<int:pk>', views.PaymentDetailView.as_view(), name='payment-detail'),

]

