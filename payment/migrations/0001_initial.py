# Generated by Django 2.1.5 on 2019-04-02 01:51

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('products', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), default=list, size=None)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_number', models.TextField()),
                ('products', django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), default=list, size=None)),
                ('coupon', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_number', models.TextField()),
                ('price', models.FloatField(default=0.0)),
                ('card_number', models.CharField(max_length=20)),
                ('token', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('billing_address', models.TextField()),
                ('billing_zipcode', models.CharField(max_length=10)),
                ('billing_city', models.CharField(max_length=50)),
                ('billing_state', models.CharField(max_length=20)),
                ('shipping_address', models.TextField()),
                ('shipping_zipcode', models.CharField(max_length=10)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField()),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('discount', models.FloatField(blank=True, default=0.0)),
            ],
        ),
    ]
