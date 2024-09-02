from .serializers import *
from rest_framework import status, generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .models import *
from .utils import process_payment


class ProductListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)

        serializer = ProductSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()
            if product:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = ProductSerializer

    lookup_field = 'pk'
    queryset = Product.objects.all()


class OrderListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order = serializer.save()
            if order:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = OrderSerializer

    lookup_field = 'pk'
    queryset = Order.objects.all()


class PaymentListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            payment = serializer.save()
            if payment:
                charge = process_payment(request.data)

                print(charge)
                data = {'success': '0', 'charge': charge}
                return Response(data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        charge_error = {'success': '1', 'charge': None}
        return Response(charge_error, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = PaymentListSerializer(queryset, many=True)
        return Response(serializer.data)


class PaymentDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = PaymentSerializer

    lookup_field = 'pk'
    queryset = Payment.objects.all()
