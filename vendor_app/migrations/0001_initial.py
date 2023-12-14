# Generated by Django 4.1.7 on 2023-12-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendorpagemodel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('vendor_code', models.CharField(blank=True, max_length=200, null=True)),
                ('on_time_delivery_rate', models.FloatField(blank=True, default=0, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, default=0, null=True)),
                ('average_response_time', models.FloatField(blank=True, default=0, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
    ]
