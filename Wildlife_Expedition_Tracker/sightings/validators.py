from django.db import models
from django.core.exceptions import ValidationError

def validate_longitude(longitude):
    if longitude < -180 or longitude > 180:
        raise ValidationError('Longitude must be between -180 and 180 degrees')

def validate_latitude(latitude):
    if latitude < -90 or latitude > 90:
        raise ValidationError('Latitude must be between -90 and 90 degrees')

def validate_time(value):
    if value:

        if value.hour > 24 or value.minute > 59:
            raise ValidationError('Invalid time. Use HH:MM format')
    return value
