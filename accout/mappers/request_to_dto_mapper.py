from accout.mappers.dto import UserDto


def request_to_dto(request):
    instance = UserDto()
    instance.first_name = request.POST.get('first_name')
    instance.last_name = request.POST.get('last_name')
    instance.phone_number = request.POST.get('phone')
    instance.email = request.POST.get('email')
    instance.username = request.POST.get('username')
    instance.password = request.POST.get('password')
    instance.confirm_password = request.POST.get('re_password')
    return instance
