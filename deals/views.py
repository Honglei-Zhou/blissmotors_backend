from .serializers import WeeklyDealSerializer, WeeklyDealListSerializer, PastDealSerializer, PastDealListSerializer
from rest_framework import status, generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .models import WeeklyDeal, PastDeal
from django_filters.rest_framework import DjangoFilterBackend


class WeeklyDealListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = WeeklyDeal.objects.all()
    serializer_class = WeeklyDealSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('current',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = WeeklyDealSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            weekly_deal = serializer.save()
            if weekly_deal:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = WeeklyDealListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class WeeklyDealDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = WeeklyDealSerializer

    lookup_field = 'pk'
    queryset = WeeklyDeal.objects.all()


class PastDealDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = PastDealSerializer

    lookup_field = 'pk'
    queryset = WeeklyDeal.objects.all()


class PastDealListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = PastDeal.objects.all()
    serializer_class = PastDealSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = PastDealSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            past_deal = serializer.save()
            if past_deal:
                # data = {'success': True, 'details': {'id': campaign.id, 'source': campaign.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = PastDealListSerializer(queryset, many=True)
        return Response(serializer.data)

