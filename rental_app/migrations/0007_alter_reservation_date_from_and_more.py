# Generated by Django 4.1 on 2023-01-07 09:05

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0006_alter_reservation_additional_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_from',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 1, 7)), django.core.validators.MinValueValidator(datetime.date(2023, 1, 7))], verbose_name='Since when?'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_to',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 1, 7)), django.core.validators.MinValueValidator(datetime.date(2023, 1, 8))], verbose_name='Until when?'),
        ),
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 1, 7)), django.core.validators.MinValueValidator(datetime.date(2023, 1, 7))], verbose_name='Since when?')),
                ('date_to', models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 1, 7)), django.core.validators.MinValueValidator(datetime.date(2023, 1, 8))], verbose_name='Until when?')),
                ('coupon', models.FloatField(choices=[(0.9, '-10%'), (0.7, '-30%'), (1, "I don't have")], verbose_name='Do you have a discount coupon?')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_app.car')),
            ],
        ),
    ]
