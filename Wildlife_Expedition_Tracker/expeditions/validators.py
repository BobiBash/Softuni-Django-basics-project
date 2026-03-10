from django.core.exceptions import ValidationError
import re


def validate_text(text):
    # Allow letters, spaces, commas, apostrophes, hyphens, and periods
    # This allows location names like "Amazon Rainforest, Brazil" or "New York"
    if not re.match(r'^[a-zA-Z\s,\'.\-]+$', text):
        raise ValidationError('This field must contain only letters, spaces, and basic punctuation.')