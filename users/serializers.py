from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import RegistrationCode, UserProfile, UserType
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from rest_auth.serializers import UserDetailsSerializer
from rest_auth.registration.serializers import RegisterSerializer
from .utils import registration_code_generator


def validate_registration_code(registration_code):
    print(registration_code)
    if len(RegistrationCode.objects.all().filter(registration_code=registration_code)) != 1:
        print(len(RegistrationCode.objects.all().filter(registration_code=registration_code)))
        raise ValidationError(
            _('%(registration_code)s does not exist.'),
            params={'registration_code': registration_code},
        )


class UserRegisterSerializer(RegisterSerializer):

    registration_code = serializers.CharField(min_length=8, required=True,
                                              validators=[UniqueValidator(queryset=UserType.objects.all()), validate_registration_code])

    def save(self, request):
        print('Here')
        user = super(UserRegisterSerializer, self).save(request)

        UserType.objects.create(user=user, registration_code=request.data['registration_code'])
        return user


class UserListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)
        ordering = ['id']


class UserSerializer(UserDetailsSerializer):
    company_name = serializers.CharField(source="userprofile.company_name", required=False, default='')
    introduction = serializers.CharField(source="userprofile.introduction", required=False, default='')
    personal_email = serializers.EmailField(source="userprofile.personal_email", required=False, default=None)
    office_phone = serializers.CharField(source="userprofile.office_phone", required=False, default='')
    mobile_phone = serializers.CharField(source="userprofile.mobile_phone", required=False, default='')
    address_1 = serializers.CharField(source="userprofile.address_1", required=False, default='')
    address_2 = serializers.CharField(source="userprofile.address_2", required=False, default='')
    address_3 = serializers.CharField(source="userprofile.address_3", required=False, default='')

    city = serializers.CharField(source="userprofile.city", required=False, default='')
    state = serializers.CharField(source="userprofile.state", required=False, default='')
    zipcode = serializers.CharField(source="userprofile.zipcode", required=False, default='')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('company_name', 'introduction', 'personal_email', 'office_phone',
                                                      'mobile_phone', 'address_1', 'address_2',
                                                      'address_3', 'city', 'state', 'zipcode',)
        read_only_fields = UserDetailsSerializer.Meta.read_only_fields + ('username',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        company_name = profile_data.get('company_name')
        introduction = profile_data.get('introduction')
        personal_email = profile_data.get('personal_email')
        office_phone = profile_data.get('office_phone')
        mobile_phone = profile_data.get('mobile_phone')
        address_1 = profile_data.get('address_1')
        address_2 = profile_data.get('address_2')
        address_3 = profile_data.get('address_3')

        city = profile_data.get('city')
        state = profile_data.get('state')
        zipcode = profile_data.get('zipcode')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = UserProfile.objects.get_or_create(user=instance)[0]

        if profile_data:
            if company_name:
                profile.company_name = company_name
            if introduction:
                profile.introduction = introduction
            if personal_email:
                profile.personal_email = personal_email
            if office_phone:
                profile.office_phone = office_phone
            if mobile_phone:
                profile.mobile_phone = mobile_phone
            if address_1:
                profile.address_1 = address_1
            if address_2:
                profile.address_2 = address_2
            if address_3:
                profile.address_3 = address_3
            if city:
                profile.city = city
            if state:
                profile.state = state
            if zipcode:
                profile.zipcode = zipcode
            profile.save()
        return instance


class RegistrationCodeListSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True
        # validators=[UniqueValidator(queryset=RegistrationCode.objects.all())]
    )

    registration_code = serializers.CharField(
        required=False
    )

    class Meta:
        model = RegistrationCode
        fields = ('id', 'email', 'registration_code')
        ordering = ['id']


class RegistrationCodeSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=RegistrationCode.objects.all())]
    )

    registration_code = serializers.CharField(
        required=False
    )

    # registration_code = serializers.CharField(
    #     required=False,
    #     validators=[UniqueValidator(queryset=RegistrationCode.objects.all())]
    # )

    def create(self, validated_data):
        registration_code = registration_code_generator('BMCM')
        while len(RegistrationCode.objects.all().filter(registration_code=registration_code)) != 0:
            registration_code = registration_code_generator('BMCM')
        registration = RegistrationCode.objects.create(email=validated_data['email'], registration_code=registration_code)
        # print(registration)
        return registration

    class Meta:
        model = RegistrationCode
        fields = ('id', 'email', 'registration_code')
        # fields = ('id', 'email')
