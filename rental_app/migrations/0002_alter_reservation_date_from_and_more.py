# Generated by Django 4.1 on 2023-01-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_from',
            field=models.DateTimeField(verbose_name='Since when?'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_to',
            field=models.DateTimeField(verbose_name='Until when?'),
        ),
    ]
