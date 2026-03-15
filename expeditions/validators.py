from django.core.exceptions import ValidationError
import re


def validate_text(text):
    if not re.match(r'^[a-zA-Z\s,\'.\-]+$', text):
        raise ValidationError('This field must contain only letters, spaces, and basic punctuation.')