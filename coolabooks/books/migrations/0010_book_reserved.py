# Generated by Django 3.1.3 on 2020-11-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20201122_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]
