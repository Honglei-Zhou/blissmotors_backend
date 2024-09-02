# Generated by Django 2.1.5 on 2019-04-02 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('office_phone', models.CharField(max_length=20)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('trim', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=30)),
                ('msrp', models.CharField(max_length=100)),
                ('sale_price', models.CharField(max_length=100)),
                ('rebate', models.CharField(max_length=100)),
                ('res', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('yearly_mileage', models.CharField(max_length=100)),
                ('money_factor', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('registration_code', models.CharField(max_length=16)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.TextField()),
                ('introduction', models.TextField()),
                ('personal_email', models.EmailField(max_length=254)),
                ('office_phone', models.CharField(max_length=20)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255)),
                ('address_3', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_code', models.CharField(max_length=16)),
                ('permission_code', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
