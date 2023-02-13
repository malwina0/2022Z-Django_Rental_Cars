# Generated by Django 4.1 on 2023-01-06 17:16

from django.db import migrations, models
import rental_app.validations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=300, validators=[rental_app.validations.validate_name, rental_app.validations.validate_is_empty]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(max_length=300, validators=[rental_app.validations.validate_name, rental_app.validations.validate_is_empty]),
        ),
    ]