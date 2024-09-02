from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import Campaign, Inquiry


class CampaignSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    phone = serializers.CharField(required=False, default='')
    first_name = serializers.CharField(required=False, default='')
    last_name = serializers.CharField(required=False, default='')

    address_1 = serializers.CharField(required=False, default='')
    address_2 = serializers.CharField(required=False, default='')
    address_3 = serializers.CharField(required=False, default='')

    city = serializers.CharField(required=False, default='')
    state = serializers.CharField(required=False, default='')
    zipcode = serializers.CharField(required=False, default='')

    source = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        email = validated_data.get('email')
        phone = validated_data.get('phone')

        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        address_1 = validated_data.get('address_1')
        address_2 = validated_data.get('address_2')
        address_3 = validated_data.get('address_3')

        city = validated_data.get('city')
        state = validated_data.get('state')
        zipcode = validated_data.get('zipcode')

        source = validated_data.get('source')

        campaign = Campaign(email=email)

        if phone:
            campaign.phone = phone
        if first_name:
            campaign.first_name = first_name
        if last_name:
            campaign.last_name = last_name
        if address_1:
            campaign.address_1 = address_1
        if address_2:
            campaign.address_2 = address_2
        if address_3:
            campaign.address_3 = address_3
        if city:
            campaign.city = city
        if state:
            campaign.state = state
        if zipcode:
            campaign.zipcode = zipcode
        if source:
            campaign.source = source
        campaign.save()
        return campaign

    class Meta:
        model = Campaign
        fields = ('id', 'email', 'phone', 'first_name', 'last_name', 'address_1', 'address_2',
                  'address_3', 'city', 'state', 'zipcode', 'source')
        # fields = ('id', 'source')


class CampaignListSerializer(serializers.ModelSerializer):

    source = serializers.CharField(required=False, default='')

    class Meta:
        model = Campaign
        fields = ('id', 'source')


class InquirySerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)

    address_1 = serializers.CharField(required=False, default='')
    address_2 = serializers.CharField(required=False, default='')
    address_3 = serializers.CharField(required=False, default='')

    city = serializers.CharField(required=False, default='')
    state = serializers.CharField(required=False, default='')
    zipcode = serializers.CharField(required=True)

    source = serializers.CharField(required=True)

    message = serializers.CharField(required=False, default='')
    year = serializers.CharField(required=False, default='')
    make = serializers.CharField(required=False, default='')
    model = serializers.CharField(required=False, default='')
    trim = serializers.CharField(required=False, default='')
    price = serializers.CharField(required=False, default='')

    cartype = serializers.CharField(required=False, default='')
    contacttype = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        email = validated_data.get('email')
        phone = validated_data.get('phone')

        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        address_1 = validated_data.get('address_1')
        address_2 = validated_data.get('address_2')
        address_3 = validated_data.get('address_3')

        city = validated_data.get('city')
        state = validated_data.get('state')
        zipcode = validated_data.get('zipcode')

        source = validated_data.get('source')

        message = validated_data.get('message')
        year = validated_data.get('year')
        make = validated_data.get('make')
        model = validated_data.get('model')
        trim = validated_data.get('trim')
        price = validated_data.get('price')
        cartype = validated_data.get('cartype')
        contacttype = validated_data.get('contacttype')

        inquiry = Inquiry(first_name=first_name, last_name=last_name,
                          email=email, phone=phone, zipcode=zipcode, source=source)

        if address_1:
            inquiry.address_1 = address_1
        if address_2:
            inquiry.address_2 = address_2
        if address_3:
            inquiry.address_3 = address_3
        if city:
            inquiry.city = city
        if state:
            inquiry.state = state
        if message:
            inquiry.message = message
        if year:
            inquiry.year = year
        if make:
            inquiry.make = make
        if model:
            inquiry.model = model
        if trim:
            inquiry.trim = trim
        if price:
            inquiry.price = price
        if cartype:
            inquiry.cartype = cartype
        if contacttype:
            inquiry.contacttype = contacttype

        inquiry.save()
        return inquiry

    class Meta:
        model = Inquiry
        fields = ('id', 'email', 'phone', 'first_name', 'last_name', 'address_1', 'address_2',
                  'address_3', 'city', 'state', 'zipcode', 'source', 'message', 'year',
                  'make', 'model', 'trim', 'price', 'cartype', 'contacttype',)
        # fields = ('id', 'source', 'message', 'year',
        #           'make', 'model', 'trim', 'price', 'cartype', 'contacttype',)


class InquiryListSerializer(serializers.ModelSerializer):

    source = serializers.CharField(required=True)

    message = serializers.CharField(required=False, default='')
    year = serializers.CharField(required=False, default='')
    make = serializers.CharField(required=False, default='')
    model = serializers.CharField(required=False, default='')
    trim = serializers.CharField(required=False, default='')
    price = serializers.CharField(required=False, default='')

    cartype = serializers.CharField(required=False, default='')
    contacttype = serializers.CharField(required=False, default='')


    class Meta:
        model = Inquiry
        fields = ('id', 'source', 'message', 'year',
                  'make', 'model', 'trim', 'price', 'cartype', 'contacttype',)
