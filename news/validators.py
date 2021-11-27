from django.core.exceptions import ValidationError


def check_to_number(value: str):
    if value.isdigit():
        raise ValidationError("Please Enter String", params={"entered_value": value})
