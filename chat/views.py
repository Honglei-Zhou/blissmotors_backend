from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .utils import detect_intent_texts

class MessageListCreateView(generics.ListCreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('session_id', 'username')
    filterset_fields = ('session_id', 'username', 'direction')
    ordering_fields = ('session_id', 'direction', 'username', 'add_time')
    ordering = ('add_time', 'session_id', 'username', 'direction')

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            message = serializer.save()
            if message:
                import json
                # resp_msg = detect_intent_texts(request.data)
                resp_msg = json.loads(request.data.get('message'))['messages'][0]
                print(resp_msg)
                data = {'success': '0', 'messages': resp_msg}
                return Response(data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = MessageSerializer

    lookup_field = 'pk'
    queryset = Message.objects.all()
