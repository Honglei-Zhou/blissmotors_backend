import django_filters
from .models import Car, CarInventory, MoneyFactor, ResidualValue


class CarFilter(django_filters.rest_framework.FilterSet):
    make = django_filters.CharFilter(field_name="make", lookup_expr='icontains')
    model = django_filters.CharFilter(field_name="model", lookup_expr='icontains')
    cartype = django_filters.CharFilter(field_name="cartype", lookup_expr='icontains')
    year = django_filters.CharFilter(field_name="year", lookup_expr='iexact')

    category = django_filters.CharFilter(field_name="category", lookup_expr='iexact')

    msrp_min = django_filters.NumberFilter(field_name="msrp_min", lookup_expr='gte')
    msrp_max = django_filters.NumberFilter(field_name="msrp_min", lookup_expr='lte')

    payment_min = django_filters.NumberFilter(field_name="payment", lookup_expr='gte')
    payment_max = django_filters.NumberFilter(field_name="payment", lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['make', 'model', 'cartype', 'category', 'year', 'payment_min', 'payment_max', 'msrp_min', 'msrp_max']


class CarInventoryFilter(django_filters.rest_framework.FilterSet):

    make = django_filters.CharFilter(field_name="make", lookup_expr='icontains')
    model = django_filters.CharFilter(field_name="model", lookup_expr='icontains')
    year = django_filters.CharFilter(field_name="year", lookup_expr='iexact')

    payment_min = django_filters.NumberFilter(field_name="payment", lookup_expr='gte')
    payment_max = django_filters.NumberFilter(field_name="payment", lookup_expr='lte')

    msrp_min = django_filters.NumberFilter(field_name="msrp", lookup_expr='gte')
    msrp_max = django_filters.NumberFilter(field_name="msrp", lookup_expr='lte')

    class Meta:
        model = CarInventory
        fields = ['make', 'model', 'year', 'payment_min', 'payment_max', 'msrp_min', 'msrp_max']


class MoneyFactorFilter(django_filters.rest_framework.FilterSet):

    make = django_filters.CharFilter(field_name="make", lookup_expr='icontains')
    model = django_filters.CharFilter(field_name="model", lookup_expr='icontains')
    trim = django_filters.CharFilter(field_name="trim", lookup_expr='icontains')

    class Meta:
        model = MoneyFactor
        fields = ['make', 'model', 'trim']


class ResidualValueFilter(django_filters.rest_framework.FilterSet):

    make = django_filters.CharFilter(field_name="make", lookup_expr='icontains')
    model = django_filters.CharFilter(field_name="model", lookup_expr='icontains')
    trim = django_filters.CharFilter(field_name="trim", lookup_expr='icontains')

    class Meta:
        model = ResidualValue
        fields = ['make', 'model', 'trim']