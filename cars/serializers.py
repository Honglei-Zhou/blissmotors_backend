from rest_framework import serializers
from .models import *


class CarMakeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    source_url = serializers.CharField(required=False, default='')
    description = serializers.CharField(required=False, default='')

    logo = serializers.CharField(required=True)

    def create(self, validated_data):

        name = validated_data.get('name')
        source_url = validated_data.get('source_url')
        description = validated_data.get('description')
        logo = validated_data.get('logo')

        car_make = CarMake(name=name, logo=logo)
        if source_url:
            car_make.source_url = source_url
        if description:
            car_make.description = description
        car_make.save()
        return car_make

    class Meta:
        model = CarMake
        fields = ('id', 'name', 'source_url', 'description', 'logo')


class CarMakeListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    logo = serializers.CharField(required=True)

    class Meta:
        model = CarMake
        fields = ('id', 'name', 'logo')


class CarModelSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    name = serializers.CharField(required=True)

    referer = serializers.CharField(required=False, default='')
    description = serializers.CharField(required=False, default='')

    logo = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        make = validated_data.get('make')
        name = validated_data.get('name')
        referer = validated_data.get('referer')
        description = validated_data.get('description')
        logo = validated_data.get('logo')

        car_model = CarModel(make=make, name=name)
        if referer:
            car_model.referer = referer
        if description:
            car_model.description = description
        if logo:
            car_model.logo = logo
        car_model.save()
        return car_model

    class Meta:
        model = CarModel
        fields = ('id', 'make', 'name', 'referer', 'description', 'logo')


class CarModelListSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    logo = serializers.CharField(required=True)

    class Meta:
        model = CarModel
        fields = ('id', 'make', 'name', 'logo')


class CarTypeSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)

    description = serializers.CharField(required=False, default='')

    logo = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        name = validated_data.get('name')
        description = validated_data.get('description')
        logo = validated_data.get('logo')

        car_type = CarType(name=name)
        if description:
            car_type.description = description
        if logo:
            car_type.logo = logo
        car_type.save()
        return car_type

    class Meta:
        model = CarType
        fields = ('id', 'name', 'description', 'logo')


class CarTypeListSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    logo = serializers.CharField(required=True)

    class Meta:
        model = CarType
        fields = ('id', 'name', 'logo')


class CarSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    mpg = serializers.CharField(required=True)
    msrp = serializers.CharField(required=True)

    cartype = serializers.CharField(required=False, default='')
    competitors = serializers.CharField(required=False, default='')

    description = serializers.CharField(required=False, default='')

    # source_url = serializers.CharField(required=False, default='')
    shopping_url = serializers.CharField(required=False, default='')
    image = serializers.CharField(required=False, default='')

    payment = serializers.FloatField(required=False, default=0.0)
    features = serializers.CharField(required=False, default='')

    # msrp_min = serializers.CharField(required=False, default='')
    # msrp_max = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        make = validated_data.get('make')
        model = validated_data.get('model')
        year = validated_data.get('year')

        mpg = validated_data.get('mpg')
        msrp = validated_data.get('msrp')

        cartype = validated_data.get('cartype')
        competitors = validated_data.get('competitors')

        description = validated_data.get('description')

        # source_url = validated_data.get('source_url')
        shopping_url = validated_data.get('shopping_url')
        image = validated_data.get('image')

        payment = validated_data.get('payment')

        features = validated_data.get('features')

        # msrp_min = validated_data.get('msrp_min')
        # msrp_max = validated_data.get('msrp_max')

        car = Car(make=make, model=model, year=year)

        if mpg:
            car.mpg = mpg
        if description:
            car.description = description
        if msrp:
            car.msrp = msrp
        if cartype:
            car.cartype = cartype
        if competitors:
            car.competitors = competitors
        # if source_url:
        #     car.source_url = source_url
        if shopping_url:
            car.shopping_url = shopping_url
        if image:
            car.image = image

        if payment:
            car.payment = payment

        if features:
            car.features = features
        # if msrp_min:
        #     car.msrp_min = msrp_min
        # if msrp_max:
        #     car.msrp_max = msrp_max
        car.save()
        return car

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'mpg', 'msrp',
                  'cartype', 'competitors', 'description', 'shopping_url', 'image', 'payment', 'features')


class CarListSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    logo = serializers.CharField(required=True)

    class Meta:
        model = Car
        fields = ('id', 'make', 'name', 'logo')


class CarImageSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    path_key = serializers.CharField(required=True)
    path_value = serializers.CharField(required=True)

    cartype = serializers.CharField(required=False, default='')
    # source_url = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        make = validated_data.get('make')
        model = validated_data.get('model')
        year = validated_data.get('year')

        path_key = validated_data.get('path_key')
        path_value = validated_data.get('path_value')

        cartype = validated_data.get('cartype')

        # source_url = validated_data.get('source_url')

        car_image = CarImage(make=make, model=model, year=year,
                       path_key=path_key, path_value=path_value)

        if cartype:
            car_image.cartype = cartype
        # if source_url:
        #     car_image.source_url = source_url

        car_image.save()
        return car_image

    class Meta:
        model = CarImage
        fields = ('id', 'make', 'model', 'year', 'path_key', 'path_value',
                  'cartype')


class CarImageListSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    path_key = serializers.CharField(required=True)
    path_value = serializers.CharField(required=True)

    class Meta:
        model = CarImage
        fields = ('id', 'make', 'model', 'year', 'path_key', 'path_value')


class CarImagePathSerializer(serializers.ModelSerializer):

    path_key = serializers.CharField(required=True)
    path_dest = serializers.CharField(required=True)

    def create(self, validated_data):

        path_key = validated_data.get('path_key')
        path_dest = validated_data.get('path_dest')

        car_image_path = CarImagePath(path_key=path_key, path_dest=path_dest)

        car_image_path.save()
        return car_image_path

    class Meta:
        model = CarImagePath
        fields = ('id', 'path_key', 'path_dest')


class CarImagePathListSerializer(serializers.ModelSerializer):
    path_key = serializers.CharField(required=True)
    path_dest = serializers.CharField(required=True)

    class Meta:
        model = CarImagePath
        fields = ('id', 'path_key', 'path_dest')


class CarSpecsSerializer(serializers.ModelSerializer):

    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    cartype = serializers.CharField(required=False, default='')

    trim = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    style = serializers.CharField(required=False, default='')

    seats = serializers.IntegerField(required=False, default='')
    doors = serializers.IntegerField(required=False, default='')
    mpg = serializers.CharField(required=False, default='')

    engine = serializers.CharField(required=False, default='')
    transmission = serializers.CharField(required=False, default='')
    drivetrain = serializers.CharField(required=False, default='')
    warranty = serializers.CharField(required=False, default='')

    source_url = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        make = validated_data.get('make')
        model = validated_data.get('model')
        cartype = validated_data.get('cartype')

        trim = validated_data.get('trim')
        year = validated_data.get('year')

        style = validated_data.get('style')

        seats = validated_data.get('seats')
        doors = validated_data.get('doors')
        mpg = validated_data.get('mpg')

        engine = validated_data.get('engine')

        transmission = validated_data.get('transmission')
        drivetrain = validated_data.get('drivetrain')
        warranty = validated_data.get('warranty')

        source_url = validated_data.get('source_url')

        car_specs = CarSpecs(make=make, model=model, trim=trim, year=year)

        if mpg:
            car_specs.mpg = mpg
        if cartype:
            car_specs.cartype = cartype
        if style:
            car_specs.style = style
        if seats:
            car_specs.seats = seats
        if doors:
            car_specs.doors = doors
        if engine:
            car_specs.engine = engine
        if transmission:
            car_specs.transmission = transmission
        if drivetrain:
            car_specs.drivetrain = drivetrain
        if warranty:
            car_specs.warranty = warranty
        if source_url:
            car_specs.source_url = source_url
        car_specs.save()
        return car_specs

    class Meta:
        model = CarSpecs
        fields = ('id', 'make', 'model', 'trim', 'cartype', 'year', 'style', 'mpg', 'seats',
                  'doors', 'engine', 'transmission', 'drivetrain', 'warranty', 'source_url')


class CarSpecsListSerializer(serializers.ModelSerializer):

    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    cartype = serializers.CharField(required=False, default='')

    trim = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    style = serializers.CharField(required=False, default='')

    seats = serializers.IntegerField(required=False, default='')
    doors = serializers.IntegerField(required=False, default='')
    mpg = serializers.CharField(required=False, default='')

    engine = serializers.CharField(required=False, default='')
    transmission = serializers.CharField(required=False, default='')
    drivetrain = serializers.CharField(required=False, default='')
    warranty = serializers.CharField(required=False, default='')

    source_url = serializers.CharField(required=False, default='')

    class Meta:
        model = CarSpecs
        fields = ('id', 'make', 'model', 'trim', 'cartype', 'year', 'style', 'mpg', 'seats',
                  'doors', 'engine', 'transmission', 'drivetrain', 'warranty', 'source_url')


class CarTrimSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    cartype = serializers.CharField(required=False, default='')

    trim = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    style = serializers.CharField(required=False, default='')

    seats = serializers.IntegerField(required=False, default='')
    msrp = serializers.CharField(required=False, default='')
    mpg = serializers.CharField(required=False, default='')

    engine = serializers.CharField(required=False, default='')
    transmission = serializers.CharField(required=False, default='')
    drivetrain = serializers.CharField(required=False, default='')

    specs_url = serializers.CharField(required=False, default='')
    source_url = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        make = validated_data.get('make')
        model = validated_data.get('model')
        cartype = validated_data.get('cartype')

        trim = validated_data.get('trim')
        year = validated_data.get('year')

        style = validated_data.get('style')

        seats = validated_data.get('seats')
        msrp = validated_data.get('msrp')
        mpg = validated_data.get('mpg')

        engine = validated_data.get('engine')

        transmission = validated_data.get('transmission')
        drivetrain = validated_data.get('drivetrain')
        specs_url = validated_data.get('specs_url')

        source_url = validated_data.get('source_url')

        car_trim = CarTrim(make=make, model=model, trim=trim, year=year)

        if mpg:
            car_trim.mpg = mpg
        if cartype:
            car_trim.cartype = cartype
        if style:
            car_trim.style = style
        if seats:
            car_trim.seats = seats
        if msrp:
            car_trim.msrp = msrp
        if engine:
            car_trim.engine = engine
        if transmission:
            car_trim.transmission = transmission
        if drivetrain:
            car_trim.drivetrain = drivetrain
        if specs_url:
            car_trim.specs_url = specs_url
        if source_url:
            car_trim.source_url = source_url
        car_trim.save()
        return car_trim

    class Meta:
        model = CarTrim
        fields = ('id', 'make', 'model', 'trim', 'cartype', 'year', 'msrp', 'style', 'mpg',
                  'seats', 'engine', 'transmission', 'drivetrain', 'specs_url', 'source_url')


class CarTrimListSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    cartype = serializers.CharField(required=False, default='')

    trim = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    style = serializers.CharField(required=False, default='')

    seats = serializers.IntegerField(required=False, default='')
    doors = serializers.IntegerField(required=False, default='')
    mpg = serializers.CharField(required=False, default='')

    engine = serializers.CharField(required=False, default='')
    transmission = serializers.CharField(required=False, default='')
    drivetrain = serializers.CharField(required=False, default='')
    warranty = serializers.CharField(required=False, default='')

    source_url = serializers.CharField(required=False, default='')

    class Meta:
        model = CarTrim
        fields = ('id', 'make', 'model', 'trim', 'cartype', 'year', 'msrp', 'style', 'mpg',
                  'seats', 'engine', 'transmission', 'drivetrain', 'specs_url', 'source_url')


class CarInventorySerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    msrp = serializers.FloatField(required=True)
    sale_price = serializers.FloatField(required=True)
    rebate = serializers.FloatField(required=True)
    res = serializers.FloatField(required=True)
    term = serializers.FloatField(required=True)

    yearly_mileage = serializers.FloatField(required=True)
    money_factor = serializers.FloatField(required=True)

    payment = serializers.FloatField(required=True)

    image = serializers.CharField(required=False, default='')

    def create(self, validated_data):

        make = validated_data.get('make')
        model = validated_data.get('model')
        year = validated_data.get('year')

        msrp = validated_data.get('msrp')

        sale_price = validated_data.get('sale_price')
        rebate = validated_data.get('rebate')
        res = validated_data.get('res')

        term = validated_data.get('term')
        yearly_mileage = validated_data.get('yearly_mileage')
        money_factor = validated_data.get('money_factor')
        payment = validated_data.get('payment')

        image = validated_data.get('image')

        car_inventory = CarInventory(make=make, model=model, year=year, msrp=msrp,
                                     sale_price=sale_price, rebate=rebate, res=res,
                                     term=term, yearly_mileage=yearly_mileage,
                                     money_factor=money_factor, payment=payment)

        if image:
            car_inventory.image = image
        car_inventory.save()
        return car_inventory

    class Meta:
        model = CarInventory
        fields = ('id', 'make', 'model', 'year', 'msrp', 'sale_price', 'rebate',
                  'res', 'term', 'yearly_mileage', 'money_factor', 'payment', 'image')


class CarInventoryListSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    year = serializers.CharField(required=True)

    class Meta:
        model = CarInventory
        fields = ('id', 'make', 'model', 'year')


class MoneyFactorSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    trim = serializers.CharField(required=True)

    mo_24 = serializers.FloatField(required=True)
    mo_27 = serializers.FloatField(required=True)
    mo_30 = serializers.FloatField(required=True)
    mo_33 = serializers.FloatField(required=True)
    mo_36 = serializers.FloatField(required=True)
    mo_39 = serializers.FloatField(required=True)
    mo_42 = serializers.FloatField(required=True)
    mo_45 = serializers.FloatField(required=True)
    mo_48 = serializers.FloatField(required=True)
    mo_51 = serializers.FloatField(required=True)
    mo_54 = serializers.FloatField(required=True)
    mo_57 = serializers.FloatField(required=True)
    mo_60 = serializers.FloatField(required=True)

    tier_4 = serializers.FloatField(required=True)
    tier_5 = serializers.FloatField(required=True)
    tier_6 = serializers.FloatField(required=True)
    tier_7 = serializers.FloatField(required=True)

    def create(self, validated_data):

        make = validated_data.get('make')
        model = validated_data.get('model')
        trim = validated_data.get('trim')

        mo_24 = validated_data.get('mo_24')
        mo_27 = validated_data.get('mo_27')
        mo_30 = validated_data.get('mo_30')
        mo_33 = validated_data.get('mo_33')
        mo_36 = validated_data.get('mo_36')
        mo_39 = validated_data.get('mo_39')
        mo_42 = validated_data.get('mo_42')
        mo_45 = validated_data.get('mo_45')
        mo_48 = validated_data.get('mo_48')
        mo_51 = validated_data.get('mo_51')
        mo_54 = validated_data.get('mo_54')
        mo_57 = validated_data.get('mo_57')
        mo_60 = validated_data.get('mo_60')

        tier_4 = validated_data.get('tier_4')
        tier_5 = validated_data.get('tier_5')
        tier_6 = validated_data.get('tier_6')
        tier_7 = validated_data.get('tier_7')

        money_factor = MoneyFactor(make=make,
                                   model=model,
                                   trim=trim,
                                   mo_24=mo_24,
                                   mo_27=mo_27,
                                   mo_30=mo_30,
                                   mo_33=mo_33,
                                   mo_36=mo_36,
                                   mo_39=mo_39,
                                   mo_42=mo_42,
                                   mo_45=mo_45,
                                   mo_48=mo_48,
                                   mo_51=mo_51,
                                   mo_54=mo_54,
                                   mo_57=mo_57,
                                   mo_60=mo_60,

                                   tier_4=tier_4,
                                   tier_5=tier_5,
                                   tier_6=tier_6,
                                   tier_7=tier_7,
                                   )

        money_factor.save()
        return money_factor

    class Meta:
        model = CarInventory
        fields = ('id',
                  'make',
                  'model',
                  'trim',
                  'mo_24',
                  'mo_27',
                  'mo_30',
                  'mo_33',
                  'mo_36',
                  'mo_39',
                  'mo_42',
                  'mo_45',
                  'mo_48',
                  'mo_51',
                  'mo_54',
                  'mo_57',
                  'mo_60',
                  'tier_4',
                  'tier_5',
                  'tier_6',
                  'tier_7',
                  )


class ResidualValueSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    trim = serializers.CharField(required=True)

    mo_24 = serializers.FloatField(required=True)
    mo_27 = serializers.FloatField(required=True)
    mo_30 = serializers.FloatField(required=True)
    mo_33 = serializers.FloatField(required=True)
    mo_36 = serializers.FloatField(required=True)
    mo_39 = serializers.FloatField(required=True)
    mo_42 = serializers.FloatField(required=True)
    mo_45 = serializers.FloatField(required=True)
    mo_48 = serializers.FloatField(required=True)
    mo_51 = serializers.FloatField(required=True)
    mo_54 = serializers.FloatField(required=True)
    mo_57 = serializers.FloatField(required=True)
    mo_60 = serializers.FloatField(required=True)

    mi_10k = serializers.FloatField(required=True)
    mi_12k = serializers.FloatField(required=True)
    mi_15k = serializers.FloatField(required=True)

    multiple_factor = serializers.IntegerField(required=True)
    multiple_mo = serializers.IntegerField(required=True)

    def create(self, validated_data):

        make = validated_data.get('make')
        model = validated_data.get('model')
        trim = validated_data.get('trim')

        mo_24 = validated_data.get('mo_24')
        mo_27 = validated_data.get('mo_27')
        mo_30 = validated_data.get('mo_30')
        mo_33 = validated_data.get('mo_33')
        mo_36 = validated_data.get('mo_36')
        mo_39 = validated_data.get('mo_39')
        mo_42 = validated_data.get('mo_42')
        mo_45 = validated_data.get('mo_45')
        mo_48 = validated_data.get('mo_48')
        mo_51 = validated_data.get('mo_51')
        mo_54 = validated_data.get('mo_54')
        mo_57 = validated_data.get('mo_57')
        mo_60 = validated_data.get('mo_60')

        mi_10k = validated_data.get('mi_10k')
        mi_12k = validated_data.get('mi_12k')
        mi_15k = validated_data.get('mi_15k')

        multiple_factor = validated_data.get('multiple_factor')
        multiple_mo = validated_data.get('multiple_mo')

        residual_value = ResidualValue(make=make,
                                       model=model,
                                       trim=trim,
                                       mo_24=mo_24,
                                       mo_27=mo_27,
                                       mo_30=mo_30,
                                       mo_33=mo_33,
                                       mo_36=mo_36,
                                       mo_39=mo_39,
                                       mo_42=mo_42,
                                       mo_45=mo_45,
                                       mo_48=mo_48,
                                       mo_51=mo_51,
                                       mo_54=mo_54,
                                       mo_57=mo_57,
                                       mo_60=mo_60,

                                       mi_10k=mi_10k,
                                       mi_12k=mi_12k,
                                       mi_15k=mi_15k,
                                       multiple_factor=multiple_factor,
                                       multiple_mo=multiple_mo
                                   )

        residual_value.save()
        return residual_value

    class Meta:
        model = CarInventory
        fields = ('id',
                  'make',
                  'model',
                  'trim',
                  'mo_24',
                  'mo_27',
                  'mo_30',
                  'mo_33',
                  'mo_36',
                  'mo_39',
                  'mo_42',
                  'mo_45',
                  'mo_48',
                  'mo_51',
                  'mo_54',
                  'mo_57',
                  'mo_60',
                  'mi_10k',
                  'mi_12k',
                  'mi_15k',
                  'multiple_factor',
                  'multiple_mo'
                  )