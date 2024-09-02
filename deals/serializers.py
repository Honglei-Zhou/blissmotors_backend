from rest_framework import serializers
from .models import WeeklyDeal, PastDeal


class WeeklyDealSerializer(serializers.ModelSerializer):
    year = serializers.CharField(required=True)
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    trim = serializers.CharField(required=False, default='')
    image = serializers.CharField(required=False, default='')

    msrp = serializers.CharField(required=True)

    monthly_payment = serializers.CharField(required=True)
    drive_off = serializers.CharField(required=False, default='0')
    other_info = serializers.CharField(required=False, default='')

    promotion_year = serializers.CharField(required=False, default='')

    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)

    current = serializers.CharField(required=True)

    def create(self, validated_data):

        year = validated_data.get('year')
        make = validated_data.get('make')
        model = validated_data.get('model')
        trim = validated_data.get('trim')

        image = validated_data.get('image')

        msrp = validated_data.get('msrp')

        monthly_payment = validated_data.get('monthly_payment')
        drive_off = validated_data.get('drive_off')
        other_info = validated_data.get('other_info')

        promotion_year = validated_data.get('promotion_year')
        start_date = validated_data.get('start_date')

        end_date = validated_data.get('end_date')

        current = validated_data.get('current')

        weekly_deal = WeeklyDeal(year=year, make=make, model=model, msrp=msrp,
                                 monthly_payment=monthly_payment, start_date=start_date, end_date=end_date)

        if trim:
            weekly_deal.trim = trim
        if image:
            weekly_deal.image = image
        if drive_off:
            weekly_deal.drive_off = drive_off
        if other_info:
            weekly_deal.other_info = other_info
        if promotion_year:
            weekly_deal.promotion_year = promotion_year
        if current:
            weekly_deal.current = current
        weekly_deal.save()
        return weekly_deal

    class Meta:
        model = WeeklyDeal
        fields = ('id', 'year', 'make', 'model', 'trim', 'image', 'msrp', 'monthly_payment',
                  'drive_off', 'other_info', 'promotion_year', 'start_date', 'end_date', 'current')
        # fields = ('id', 'source')


class WeeklyDealListSerializer(serializers.ModelSerializer):

    year = serializers.CharField(required=True)
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    trim = serializers.CharField(required=False, default='')
    image = serializers.CharField(required=False, default='')

    class Meta:
        model = WeeklyDeal
        fields = ('id', 'year', 'make', 'model', 'trim', 'image',)


class PastDealSerializer(serializers.ModelSerializer):
    year = serializers.CharField(required=True)
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    trim = serializers.CharField(required=False, default='')
    image = serializers.CharField(required=False, default='')

    msrp = serializers.CharField(required=True)

    monthly_payment = serializers.CharField(required=True)
    drive_off = serializers.CharField(required=False, default='0')
    other_info = serializers.CharField(required=False, default='')

    promotion_year = serializers.CharField(required=False, default='')

    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)

    current = serializers.CharField(required=True)

    def create(self, validated_data):

        year = validated_data.get('year')
        make = validated_data.get('make')
        model = validated_data.get('model')
        trim = validated_data.get('trim')

        image = validated_data.get('image')

        msrp = validated_data.get('msrp')

        monthly_payment = validated_data.get('monthly_payment')
        drive_off = validated_data.get('drive_off')
        other_info = validated_data.get('other_info')

        promotion_year = validated_data.get('promotion_year')
        start_date = validated_data.get('start_date')

        end_date = validated_data.get('end_date')

        current = validated_data.get('current')

        weekly_deal = WeeklyDeal(year=year, make=make, model=model, msrp=msrp,
                                 monthly_payment=monthly_payment, start_date=start_date, end_date=end_date)

        if trim:
            weekly_deal.trim = trim
        if image:
            weekly_deal.image = image
        if drive_off:
            weekly_deal.drive_off = drive_off
        if other_info:
            weekly_deal.other_info = other_info
        if promotion_year:
            weekly_deal.promotion_year = promotion_year
        if current:
            weekly_deal.current = current
        weekly_deal.save()
        return weekly_deal

    class Meta:
        model = PastDeal
        fields = ('id', 'year', 'make', 'model', 'trim', 'image', 'msrp', 'monthly_payment',
                  'drive_off', 'other_info', 'promotion_year', 'start_date', 'end_date', 'current')
        # fields = ('id', 'source')


class PastDealListSerializer(serializers.ModelSerializer):
    year = serializers.CharField(required=True)
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    trim = serializers.CharField(required=False, default='')
    image = serializers.CharField(required=False, default='')

    msrp = serializers.CharField(required=True)

    monthly_payment = serializers.CharField(required=True)
    drive_off = serializers.CharField(required=False, default='0')
    other_info = serializers.CharField(required=False, default='')

    promotion_year = serializers.CharField(required=False, default='')

    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)

    class Meta:
        model = PastDeal
        fields = ('id', 'year', 'make', 'model', 'trim', 'image', 'msrp', 'monthly_payment',
                  'drive_off', 'other_info', 'promotion_year', 'start_date', 'end_date',)