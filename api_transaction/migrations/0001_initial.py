# Generated by Django 3.2 on 2021-05-04 05:04

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
            name='Office_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('designation_date', models.DateTimeField()),
                ('designationID', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=16)),
                ('birth_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TaxPeriodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_type', models.CharField(max_length=100)),
                ('period_duration', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaxSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_field', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=250)),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('requisition', models.FloatField()),
                ('tax', models.FloatField(default=0)),
                ('vat', models.FloatField(default=0)),
                ('transaction_cost', models.FloatField(default=0)),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxID', models.CharField(blank=True, max_length=500, null=True)),
                ('tax_paid_date', models.DateTimeField(blank=True, null=True)),
                ('tax_paid_amt', models.FloatField(blank=True, null=True)),
                ('tax_info_law', models.TextField(blank=True, null=True)),
                ('tax_given_area', models.TextField(blank=True, null=True)),
                ('tax_medium', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_office_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_transaction.office_person')),
                ('taxperiodtype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_transaction.taxperiodtype')),
                ('withdraw', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wthdrw', to='api_transaction.withdraw')),
            ],
        ),
    ]
