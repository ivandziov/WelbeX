from functools import wraps

from django.core.exceptions import ValidationError
from typing import Callable


def validate_range(min_value: int, max_value: int) -> Callable:
    @wraps(validate_range)
    def validator(value: int) -> None:
        if not min_value <= value <= max_value:
            raise ValidationError(f'The number should be in the interval {min_value, max_value}')

    return validator
