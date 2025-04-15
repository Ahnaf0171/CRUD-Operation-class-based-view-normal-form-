# Generated by Django 5.2 on 2025-04-13 12:43

import new_gadget.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gadget_table',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to=new_gadget.models.image_add)),
                ('price', models.IntegerField()),
                ('about', models.CharField(max_length=2000)),
            ],
        ),
    ]
