from django.core.exceptions import ValidationError


def validate_car_number(value: str) -> None:
    if not isinstance(value, str):
        raise ValidationError('The value must be a string!')

    if len(value) != 5:
        raise ValidationError('The value must contain 5 characters!')

    if (not value[:4].isdigit()) or (not value[4].isupper()) or (not 'A' <= value[4] <= 'Z'):
        raise ValidationError('The value must contain an English capital letter at the end!')

    print(int(value[:4]))
    if not 1000 <= int(value[:4]) <= 9999:
        raise ValidationError('The number must be in the range from 1000 to 9999 inclusive!')