import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm, widgets, Form, models
from django import forms
from .models import Car, Reservation, Calculation
from .validations import add_years


class CreateCarForm(ModelForm):
    class Meta:
        model = Car
        fields = [
            "car_model",
            "price",
            "production_year",
            "engine_size",
            "horsepower",
            "description",
            "gearbox",
        ]


class RentACarForm(ModelForm):
    class Meta:
        model = Reservation
        widgets = {
            'date_from': forms.DateInput(attrs={
                'type': 'date',
            }),
            'date_to': forms.DateInput(attrs={
                'type': 'date',
            }),
        }
        fields = [
            'car',
            'date_from',
            'date_to',
            'driver_licence_img',
            'driver_licence_length',
            'additional_info'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['additional_info'].required = False
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})

    def clean(self):
        super().clean()

        date_from = self.cleaned_data.get('date_from')
        date_to = self.cleaned_data.get('date_to')
        if date_to == date_from:
            self._errors['data_to'] = self.error_class(['You have to make a reservation for at least 1 day.'])
        elif date_to < date_from:
            self._errors['data_to'] = self.error_class(['The end date of the reservation must be later than the start '
                                                        'date.'])

        return self.cleaned_data


class PriceCalculatorForm(ModelForm):
    class Meta:
        model = Calculation
        fields = ('car', 'date_from', 'date_to', 'coupon')
        widgets = {
            'date_from': forms.DateInput(attrs={
                'type': 'date',
            }),
            'date_to': forms.DateInput(attrs={
                'type': 'date',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})
