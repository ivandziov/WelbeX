from django.core.validators import RegexValidator

POSTAL_CODE_VALIDATOR = RegexValidator('^[0-9]{6}$', 'Invalid postal code')
