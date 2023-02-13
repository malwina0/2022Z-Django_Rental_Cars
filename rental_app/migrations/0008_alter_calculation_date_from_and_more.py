# Generated by Django 4.1 on 2023-02-13 16:46

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0007_alter_reservation_date_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='date_from',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 2, 13)), django.core.validators.MinValueValidator(datetime.date(2023, 2, 13))], verbose_name='Since when?'),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='date_to',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 2, 13)), django.core.validators.MinValueValidator(datetime.date(2023, 2, 14))], verbose_name='Until when?'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_from',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 2, 13)), django.core.validators.MinValueValidator(datetime.date(2023, 2, 13))], verbose_name='Since when?'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_to',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 2, 13)), django.core.validators.MinValueValidator(datetime.date(2023, 2, 14))], verbose_name='Until when?'),
        ),
    ]
