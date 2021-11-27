from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from accout.mappers.dto import UserDto
from accout.models import Employee


def to_user_model(dto: UserDto):
    user = User()
    user.username = dto.username
    user.password = make_password(dto.password)
    user.first_name = dto.first_name
    user.last_name = dto.last_name
    user.email = dto.email
    user.is_active = 1
    return user


def to_employee_model(dto: UserDto):
    employee = Employee()
    employee.phone = dto.phone_number
    return employee
