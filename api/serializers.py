from rest_framework import serializers
from .models import Car
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class CarSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'cartype', 'year', 'links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('car-detail', kwargs = {
                'pk': obj.pk
            }, request=request)
        }
