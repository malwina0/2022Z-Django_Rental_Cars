import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from rental_app.validations import add_years, validate_file_extension
from users.models import MyUser


class Car(models.Model):
    car_brand = models.CharField(max_length=150, default='')
    car_model = models.CharField(max_length=150)
    price = models.IntegerField()
    production_year = models.IntegerField(validators=[
        MaxValueValidator(datetime.datetime.now().year),
        MinValueValidator(1900)
    ])
    engine_size = models.IntegerField()
    horsepower = models.IntegerField()
    description = models.CharField(max_length=4000, default='')
    GEARBOX_CHOICES = [
        ('AUTO', 'automatic'),
        ('MANUAL', 'manual'),
    ]
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES, default='AUTO')  # skrzynia biegow
    image = models.ImageField(upload_to='uploads/', default='')

    def __str__(self):
        return self.car_brand + " " + self.car_model


class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None, verbose_name='Which car you want to rent?')
    date_from = models.DateField(verbose_name='Since when?',
                                 validators=[
                                     MaxValueValidator(add_years(datetime.date.today(), 1)),
                                     MinValueValidator(datetime.date.today())
                                 ]
                                 )
    date_to = models.DateField(verbose_name='Until when?',
                               validators=[
                                   MaxValueValidator(add_years(datetime.date.today(), 1)),
                                   MinValueValidator(datetime.date.today() + datetime.timedelta(days=1))
                               ]
                               )
    user = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE)
    additional_info = models.TextField(verbose_name='If you have any additional comments, please '
                                                    'write us here about it.')
    driver_licence_length = models.IntegerField(verbose_name="How long have you held your driver's license? (in years)",
                                                validators=[
                                                    MaxValueValidator(100),
                                                    MinValueValidator(0)
                                                ],
                                                default=0
                                                )
    driver_licence_img = models.FileField(verbose_name="Send a scan of your driver's license.",
                                          upload_to='uploads/driver_licences',
                                          validators=[validate_file_extension]
                                          )

    def __str__(self):
        return f'{self.car}: {self.date_from} - {self.date_to} ({self.user})'


class Calculation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_from = models.DateField(verbose_name='Since when?',
                                 validators=[
                                     MaxValueValidator(add_years(datetime.date.today(), 1)),
                                     MinValueValidator(datetime.date.today())
                                 ],
                                 )
    date_to = models.DateField(verbose_name='Until when?',
                               validators=[
                                   MaxValueValidator(add_years(datetime.date.today(), 1)),
                                   MinValueValidator(datetime.date.today() + datetime.timedelta(days=1))
                               ]
                               )
    couponChoices = [(0.9, '-10%'),
                     (0.7, '-30%'),
                     (1, "I don't have")]
    coupon = models.FloatField(choices=couponChoices,
                               verbose_name='Do you have a discount coupon?')