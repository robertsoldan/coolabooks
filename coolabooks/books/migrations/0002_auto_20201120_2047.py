# Generated by Django 3.1.2 on 2020-11-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(),
        ),
    ]
