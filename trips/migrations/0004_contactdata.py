# Generated by Django 3.0.3 on 2020-06-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
