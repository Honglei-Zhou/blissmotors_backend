from .models import RegistrationCode
from .serializers import UserListSerializer, RegistrationCodeSerializer, RegistrationCodeListSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserList(generics.ListAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    queryset = User.objects.all().order_by('id')
    serializer_class = UserListSerializer


class RegistrationCodeView(generics.RetrieveAPIView):
    queryset = RegistrationCode.objects.all()
    serializer_class = RegistrationCodeSerializer
    lookup_field = 'pk'


class RegistrationCodeCreateView(generics.ListCreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = RegistrationCode.objects.all().order_by('id')
    serializer_class = RegistrationCodeSerializer

    # def get(self, request, pk):
    #     registration = get_object_or_404(RegistrationCode, pk=pk)
    #     serializer = RegistrationCodeSerializer(registration)
    #     return Response({'serializer': serializer, 'registration_code': registration.registration_code})

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = RegistrationCodeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            registration = serializer.save()
            if registration:
                mail_subject = 'Bliss Lease Website Registration Code'
                message = 'Hi\n' \
                          'Your registration is code : {}\n' \
                          'Please use the following email: {} to register.'.format(registration.registration_code, registration.email)

                to_email = registration.email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                # data = {'email': registration.email, 'registration_code': registration.registration_code}
                # print(data)
                # print(type(serializer.data))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        '''
        This method could be overriden to fulfil specific purposes.
        '''
        queryset = self.get_queryset()
        serializer = RegistrationCodeListSerializer(queryset, many=True)
        return Response(serializer.data)
