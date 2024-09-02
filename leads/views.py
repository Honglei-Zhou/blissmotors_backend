from django.shortcuts import render, get_object_or_404
from .serializers import InquirySerializer, CampaignSerializer, InquiryListSerializer, CampaignListSerializer
from rest_framework import status, generics, views
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .models import Inquiry, Campaign


# Create your views here.
class InquiryView(generics.CreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = InquirySerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = InquirySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            inquiry = serializer.save()
            if inquiry:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignView(generics.CreateAPIView):
    serializer_class = CampaignSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            campaign = serializer.save()
            if campaign:
                # data = {'success': True, 'details': {'id': campaign.id, 'source': campaign.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InquiryDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = InquirySerializer
    queryset = Inquiry.objects.all()
    lookup_field = 'pk'


class CampaignDetailView(generics.RetrieveUpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    lookup_field = 'pk'


class InquiryListCreate(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Inquiry.objects.all()
    serializer_class = InquiryListSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = InquirySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            inquiry = serializer.save()
            if inquiry:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = CampaignListSerializer(queryset, many=True)
        return Response(serializer.data)


class CampaignListCreate(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            campaign = serializer.save()
            if campaign:
                # data = {'success': True, 'details': {'id': campaign.id, 'source': campaign.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = CampaignListSerializer(queryset, many=True)
        return Response(serializer.data)
