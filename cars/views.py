from .serializers import *
from rest_framework import status, generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .models import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filter import *


class CarsPagination(PageNumberPagination):

    page_size = 16
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class CarMakeListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarMake.objects.all().order_by('name')
    serializer_class = CarMakeSerializer
    pagination_class = CarsPagination

    # filter_backends = (DjangoFilterBackend)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarMakeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car_make = serializer.save()
            if car_make:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = CarMakeListSerializer(queryset, many=True)
        return Response(serializer.data)


class CarMakeDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarMakeSerializer

    lookup_field = 'pk'
    queryset = CarMake.objects.all()


class CarModelListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    pagination_class = CarsPagination

    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('make', 'name')
    ordering_fields = ('make', 'name')
    ordering = ('make', 'name',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car_model = serializer.save()
            if car_model:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarModelListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarModelDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarModelSerializer

    lookup_field = 'pk'
    queryset = CarModel.objects.all()


class CarTypeListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarType.objects.all().order_by('id')
    serializer_class = CarTypeSerializer
    pagination_class = CarsPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarMakeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car_type = serializer.save()
            if car_type:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarTypeListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarTypeDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarTypeSerializer

    lookup_field = 'pk'
    queryset = CarType.objects.all()


class CarTrimListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarTrim.objects.all().order_by('id')
    serializer_class = CarTrimSerializer
    pagination_class = CarsPagination

    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('make', 'model', 'trim')
    filterset_fields = ('make', 'model', 'trim', 'year')

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarTrimSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car_trim = serializer.save()
            if car_trim:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarTrimListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarTrimDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarTrimSerializer

    lookup_field = 'pk'
    queryset = CarTrim.objects.all()


class CarSpecsListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarSpecs.objects.all().order_by('id')
    serializer_class = CarSpecsSerializer
    pagination_class = CarsPagination

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarSpecsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car_specs = serializer.save()
            if car_specs:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarSpecsListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarSpecsDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarSpecsSerializer

    lookup_field = 'pk'
    queryset = CarSpecs.objects.all()


class CarImageListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarImage.objects.all().order_by('path_name')
    serializer_class = CarImageSerializer
    pagination_class = CarsPagination

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('make', 'model', 'year')

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarSpecsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car_image = serializer.save()
            if car_image:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarImageListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarImageDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarImageSerializer

    lookup_field = 'pk'
    queryset = CarImage.objects.all()


class CarImagePathListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarImagePath.objects.all().order_by('id')
    serializer_class = CarImagePathSerializer
    pagination_class = CarsPagination

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarImagePathSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car_image_path = serializer.save()
            if car_image_path:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarImagePathListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarImagePathDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarImagePathSerializer

    lookup_field = 'pk'
    queryset = CarImagePath.objects.all()


class CarListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = CarsPagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_class = CarFilter
    ordering_fields = ('make', 'model')
    ordering = ('make', 'model',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car = serializer.save()
            if car:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarSerializer

    lookup_field = 'pk'
    queryset = Car.objects.all()


class CarInventoryListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = CarInventory.objects.all()
    serializer_class = CarInventorySerializer
    pagination_class = CarsPagination

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_class = CarInventoryFilter
    ordering_fields = ('payment', 'make', 'model')
    ordering = ('payment', 'make', 'model',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CarInventorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            car = serializer.save()
            if car:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = CarListSerializer(queryset, many=True)
    #     return Response(serializer.data)


class CarInventoryDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = CarInventorySerializer

    lookup_field = 'pk'
    queryset = CarInventory.objects.all()


class MoneyFactorListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = MoneyFactor.objects.all()
    serializer_class = MoneyFactorSerializer


    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_class = MoneyFactorFilter
    ordering_fields = ('make', 'model',)
    ordering = ('make', 'model',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = MoneyFactorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            money_factor = serializer.save()
            if money_factor:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoneyFactorDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = MoneyFactorSerializer

    lookup_field = 'pk'
    queryset = MoneyFactor.objects.all()


class ResidualValueListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = ResidualValue.objects.all()
    serializer_class = ResidualValueSerializer


    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_class = ResidualValueFilter
    ordering_fields = ('make', 'model',)
    ordering = ('make', 'model',)

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = MoneyFactorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            residual_value = serializer.save()
            if residual_value:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResidualValueDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = ResidualValueSerializer

    lookup_field = 'pk'
    queryset = ResidualValue.objects.all()