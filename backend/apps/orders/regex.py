from enum import Enum


class OrderValidationRegex(Enum):

    NAME_SURNAME = (
        r"^[A-ZА-ЯІЇЄҐ][a-zа-яіїєґ']{1,29}$",
        "Must start with a capital letter and contain only the letters"
    )

    PHONE_NUMBER = (
        r"^\+?380\d{9}$",
        "The number format must be as follows: +380501234567, 380501234567"
    )

    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg
