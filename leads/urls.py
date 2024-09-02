from django.urls import path
from . import views

urlpatterns = [
    # path('campaigns', views.CampaignView.as_view(), name='campaign-create'),
    path('campaigns', views.CampaignListCreate.as_view(), name='campaign-listcreate'),
    path('campaigns/<int:pk>', views.CampaignDetailView.as_view(), name='campaign-detail'),
    # path('inquiries', views.InquiryView.as_view(), name='inquiry-create'),
    path('inquiries/<int:pk>', views.InquiryDetailView.as_view(), name='inquiry-detail'),
    path('inquiries', views.InquiryListCreate.as_view(), name='inquiry-listcreate'),
]


