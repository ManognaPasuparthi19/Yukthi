# Generated by Django 2.2.1 on 2019-06-04 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_hydbdaydecoration_hydbdaygifts_hydhalls'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hydbdaycakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('decorationname', models.CharField(max_length=30)),
                ('decorationtype', models.CharField(max_length=30)),
                ('avilable', models.CharField(choices=[('avilable', 'yes'), ('unavilable', 'no')], max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('noofitems', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
