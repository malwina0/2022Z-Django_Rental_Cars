# functions used to validate the data
from datetime import datetime
import os
from django.core.exceptions import ValidationError
import re


def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please attach a file in one of these formats: .pdf, .doc, .docx, .jpg, .png.')


def validate_is_empty(msg):
    # Check if string is empty or contain spaces only
    if not msg or re.search("^\s*$", msg):
        raise ValidationError('This filed cannot be empty or contain only spaces.')


def validate_phone_number(number):
    # check if it contains 9-11 digitd
    if not (1000000000000 > number > 100000000):
        raise ValidationError('Phone number must contain 9-11 digits.')


def validate_name(name):
    pattern = re.compile("^([A-Za-z/-]*)$")
    if not pattern.match(name):
        raise ValidationError('Only letters and "-" are allowed in your name.')
