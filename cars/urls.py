from django.urls import include, path
from . import views

urlpatterns = [
    path('carmakes/', views.CarMakeListCreateView.as_view()),
    path('carmakes/<int:pk>', views.CarMakeDetailView.as_view()),

    path('carmodels/', views.CarModelListCreateView.as_view()),
    path('carmodels/<int:pk>', views.CarModelDetailView.as_view()),

    path('cartypes/', views.CarTypeListCreateView.as_view()),
    path('cartypes/<int:pk>', views.CarTypeDetailView.as_view()),

    path('cartrims/', views.CarTrimListCreateView.as_view()),
    path('cartrims/<int:pk>', views.CarTrimDetailView.as_view()),

    path('carspecs/', views.CarSpecsListCreateView.as_view()),
    path('carspecs/<int:pk>', views.CarSpecsDetailView.as_view()),

    path('carimagepaths/', views.CarImagePathListCreateView.as_view()),
    path('carimagepaths/<int:pk>', views.CarImagePathDetailView.as_view()),

    path('carimages/', views.CarImageListCreateView.as_view()),
    path('carimages/<int:pk>', views.CarImageDetailView.as_view()),

    path('cars/', views.CarListCreateView.as_view()),
    path('cars/<int:pk>', views.CarDetailView.as_view()),

    path('carinventory/', views.CarInventoryListCreateView.as_view()),
    path('carinventory/<int:pk>', views.CarInventoryDetailView.as_view()),
]


