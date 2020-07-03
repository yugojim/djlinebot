# Generated by Django 3.0.3 on 2020-06-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_contactdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='predict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predict_date', models.DateTimeField(auto_now_add=True)),
                ('nasdaq_open', models.CharField(max_length=50)),
                ('nasdaq_high', models.CharField(max_length=50)),
                ('nasdaq_low', models.CharField(max_length=50)),
                ('nasdaq_close', models.CharField(max_length=50)),
                ('nasdaq_adjclose', models.CharField(max_length=50)),
                ('nasdaq_volume', models.CharField(max_length=50)),
                ('dowjons_open', models.CharField(max_length=50)),
                ('dowjons_high', models.CharField(max_length=50)),
                ('dowjons_low', models.CharField(max_length=50)),
                ('dowjons_close', models.CharField(max_length=50)),
                ('dowjons_adjclose', models.CharField(max_length=50)),
                ('dowjons_volume', models.CharField(max_length=50)),
                ('sp500_open', models.CharField(max_length=50)),
                ('sp500_high', models.CharField(max_length=50)),
                ('sp500_low', models.CharField(max_length=50)),
                ('sp500_close', models.CharField(max_length=50)),
                ('sp500_adjclose', models.CharField(max_length=50)),
                ('sp500_volume', models.CharField(max_length=50)),
                ('twii_open', models.CharField(max_length=50)),
                ('twii_high', models.CharField(max_length=50)),
                ('twii_low', models.CharField(max_length=50)),
                ('twii_close', models.CharField(max_length=50)),
                ('twii_adjclose', models.CharField(max_length=50)),
                ('twii_volume', models.CharField(max_length=50)),
                ('tsegradientopen', models.CharField(max_length=50)),
                ('tsegradienthigh', models.CharField(max_length=50)),
                ('tsegradientlow', models.CharField(max_length=50)),
                ('tsegradientclose', models.CharField(max_length=50)),
                ('tselinearopen', models.CharField(max_length=50)),
                ('tselinearhigh', models.CharField(max_length=50)),
                ('tselinearlow', models.CharField(max_length=50)),
                ('tselinearclose', models.CharField(max_length=50)),
                ('tserandomforestopen', models.CharField(max_length=50)),
                ('tserandomforesthigh', models.CharField(max_length=50)),
                ('tserandomforestlow', models.CharField(max_length=50)),
                ('tserandomforestclose', models.CharField(max_length=50)),
            ],
        ),
    ]
