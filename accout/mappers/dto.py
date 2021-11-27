class UserDto:

    def __init__(self, first_name=None,
                 last_name=None, phone_number=None,
                 email=None, username=None,
                 password=None, confirm_password=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

