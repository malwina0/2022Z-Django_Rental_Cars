# Generated by Django 4.1 on 2023-01-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0002_alter_reservation_date_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_from',
            field=models.DateField(verbose_name='Since when?'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_to',
            field=models.DateField(verbose_name='Until when?'),
        ),
    ]
