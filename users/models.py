from django.db import models
from django.contrib.auth.models import AbstractUser
from rental_app.validations import validate_is_empty, validate_phone_number, validate_name


class MyUser(AbstractUser):
    STATUS = (('regular', 'regular'),
              ('moderator', 'moderator'))
    first_name = models.CharField(validators=[validate_name, validate_is_empty], max_length=300)
    last_name = models.CharField(validators=[validate_name, validate_is_empty], max_length=300)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=50, choices=STATUS, default='regular')
    phone = models.IntegerField(default=0,
                                validators=[validate_phone_number]
                                )
    birth_date = models.DateField(default='1990-01-01')


    def __str__(self):
        return self.username
