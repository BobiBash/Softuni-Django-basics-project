from django.core.exceptions import ValidationError


def validate_text(text):
    if not text.isalpha():
        raise ValidationError('This field must contain only letters.')