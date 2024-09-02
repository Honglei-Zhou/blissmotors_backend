from django.shortcuts import render, get_object_or_404
from .serializers import JobSerializer, JobListSerializer, JobApplicantSerializer, JobApplicantListSerializer
from rest_framework import status, generics
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .models import Job, JobApplicant


class JobDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'pk'


class JobApplicantDetailView(generics.RetrieveUpdateAPIView):
    queryset = JobApplicant.objects.all()
    serializer_class = JobApplicantSerializer
    lookup_field = 'pk'


class JobListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            job = serializer.save()
            if job:
                # data = {'success': True, 'details': {'id': inquiry.id, 'source': inquiry.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer =JobListSerializer(queryset, many=True)
        return Response(serializer.data)


class JobApplicantListCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = JobApplicant.objects.all()
    serializer_class = JobApplicantSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = JobApplicantSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            job_applicant = serializer.save()
            if job_applicant:
                # data = {'success': True, 'details': {'id': campaign.id, 'source': campaign.source}}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     '''
    #     This method could be overriden to fulfil specific purposes.
    #     '''
    #     queryset = self.get_queryset()
    #     serializer = JobApplicantListSerializer(queryset, many=True)
    #     return Response(serializer.data)
